import re
import os
from collections import Counter

class ContadorPalavras:
    def __init__(self):
        self.conteudo = ""
        self.palavras = []
        self.contador = Counter()
        self.estatisticas = {}

    def ler_arquivo(self, caminho):
        """Lê o arquivo e armazena o conteúdo"""
        try:
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                self.conteudo = arquivo.read()
            print(f"✅ Arquivo '{os.path.basename(caminho)}' carregado com sucesso!")
            return True
        except FileNotFoundError:
            print("❌ Arquivo não encontrado. Verifique o caminho e tente novamente.")
            return False
        except UnicodeDecodeError:
            print("❌ Erro de codificação. Tente um arquivo com codificação UTF-8.")
            return False
        except Exception as e:
            print(f"❌ Erro ao ler arquivo: {e}")
            return False

    def processar_texto(self):
        """Processa o texto e extrai as palavras"""
        if not self.conteudo:
            print("❌ Nenhum conteúdo para processar.")
            return False
        
        # Separar em palavras (considerando apenas letras e números)
        self.palavras = re.findall(r'\b\w+\b', self.conteudo.lower())
        self.contador = Counter(self.palavras)
        
        # Calcular estatísticas
        self.estatisticas = {
            'total_palavras': len(self.palavras),
            'palavras_unicas': len(self.contador),
            'caracteres': len(self.conteudo),
            'linhas': len(self.conteudo.splitlines()),
            'palavra_mais_frequente': self.contador.most_common(1)[0] if self.contador else None
        }
        
        return True

    def exibir_estatisticas_gerais(self):
        """Exibe estatísticas gerais do texto"""
        print("\n" + "="*50)
        print("📊 ESTATÍSTICAS GERAIS")
        print("="*50)
        print(f"📝 Total de palavras: {self.estatisticas['total_palavras']}")
        print(f"🔤 Palavras únicas: {self.estatisticas['palavras_unicas']}")
        print(f"📏 Total de caracteres: {self.estatisticas['caracteres']}")
        print(f"📄 Total de linhas: {self.estatisticas['linhas']}")
        
        if self.estatisticas['palavra_mais_frequente']:
            palavra, freq = self.estatisticas['palavra_mais_frequente']
            print(f"⭐ Palavra mais frequente: '{palavra}' ({freq} vezes)")

    def exibir_palavras_frequentes(self, quantidade=10):
        """Exibe as palavras mais frequentes"""
        print(f"\n📈 TOP {quantidade} PALAVRAS MAIS FREQUENTES")
        print("-" * 40)
        for i, (palavra, frequencia) in enumerate(self.contador.most_common(quantidade), 1):
            print(f"{i:2d}. {palavra:<20} ({frequencia:3d} vezes)")

    def buscar_palavra(self, palavra):
        """Busca uma palavra específica no texto"""
        palavra_lower = palavra.lower()
        if palavra_lower in self.contador:
            print(f"✅ Palavra '{palavra}' encontrada {self.contador[palavra_lower]} vezes")
        else:
            print(f"❌ Palavra '{palavra}' não encontrada no texto")

    def filtrar_palavras_por_tamanho(self, tamanho_minimo=1, tamanho_maximo=100):
        """Filtra palavras por tamanho"""
        palavras_filtradas = [p for p in self.palavras if tamanho_minimo <= len(p) <= tamanho_maximo]
        contador_filtrado = Counter(palavras_filtradas)
        
        print(f"\n🔍 PALAVRAS COM {tamanho_minimo}-{tamanho_maximo} CARACTERES")
        print("-" * 50)
        for palavra, freq in contador_filtrado.most_common(10):
            print(f"{palavra:<20} ({freq:3d} vezes)")

    def salvar_relatorio(self, nome_arquivo="relatorio_palavras.txt"):
        """Salva um relatório completo em arquivo"""
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write("RELATÓRIO DE ANÁLISE DE TEXTO\n")
                arquivo.write("="*50 + "\n\n")
                
                arquivo.write("ESTATÍSTICAS GERAIS:\n")
                arquivo.write(f"Total de palavras: {self.estatisticas['total_palavras']}\n")
                arquivo.write(f"Palavras únicas: {self.estatisticas['palavras_unicas']}\n")
                arquivo.write(f"Total de caracteres: {self.estatisticas['caracteres']}\n")
                arquivo.write(f"Total de linhas: {self.estatisticas['linhas']}\n\n")
                
                arquivo.write("PALAVRAS MAIS FREQUENTES:\n")
                for palavra, freq in self.contador.most_common(20):
                    arquivo.write(f"{palavra}: {freq}\n")
            
            print(f"✅ Relatório salvo em '{nome_arquivo}'")
        except Exception as e:
            print(f"❌ Erro ao salvar relatório: {e}")

def menu_principal():
    """Menu principal da aplicação"""
    contador = ContadorPalavras()
    
    while True:
        print("\n" + "="*60)
        print("📚 CONTADOR DE PALAVRAS - MENU PRINCIPAL")
        print("="*60)
        print("1. 📁 Carregar arquivo de texto")
        print("2. 📊 Exibir estatísticas gerais")
        print("3. 📈 Exibir palavras mais frequentes")
        print("4. 🔍 Buscar palavra específica")
        print("5. 🔧 Filtrar palavras por tamanho")
        print("6. 💾 Salvar relatório")
        print("7. ❌ Sair")
        print("-"*60)
        
        opcao = input("Escolha uma opção (1-7): ").strip()
        
        if opcao == "1":
            caminho = input("Digite o caminho do arquivo: ").strip()
            if contador.ler_arquivo(caminho):
                contador.processar_texto()
        
        elif opcao == "2":
            if contador.conteudo:
                contador.exibir_estatisticas_gerais()
            else:
                print("❌ Carregue um arquivo primeiro!")
        
        elif opcao == "3":
            if contador.conteudo:
                try:
                    qtd = int(input("Quantas palavras exibir? (padrão: 10): ") or "10")
                    contador.exibir_palavras_frequentes(qtd)
                except ValueError:
                    contador.exibir_palavras_frequentes()
            else:
                print("❌ Carregue um arquivo primeiro!")
        
        elif opcao == "4":
            if contador.conteudo:
                palavra = input("Digite a palavra para buscar: ").strip()
                if palavra:
                    contador.buscar_palavra(palavra)
            else:
                print("❌ Carregue um arquivo primeiro!")
        
        elif opcao == "5":
            if contador.conteudo:
                try:
                    min_len = int(input("Tamanho mínimo (padrão: 1): ") or "1")
                    max_len = int(input("Tamanho máximo (padrão: 100): ") or "100")
                    contador.filtrar_palavras_por_tamanho(min_len, max_len)
                except ValueError:
                    print("❌ Digite números válidos!")
            else:
                print("❌ Carregue um arquivo primeiro!")
        
        elif opcao == "6":
            if contador.conteudo:
                nome_arquivo = input("Nome do arquivo de relatório (padrão: relatorio_palavras.txt): ").strip()
                if not nome_arquivo:
                    nome_arquivo = "relatorio_palavras.txt"
                contador.salvar_relatorio(nome_arquivo)
            else:
                print("❌ Carregue um arquivo primeiro!")
        
        elif opcao == "7":
            print("👋 Obrigado por usar o Contador de Palavras!")
            break
        
        else:
            print("❌ Opção inválida! Escolha entre 1-7.")

if __name__ == "__main__":
    menu_principal()
