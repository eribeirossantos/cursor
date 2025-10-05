#criar uma calculadora com as seguintes funcionalidades:
# 1. Adição
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Operações disponíveis: + (adição), - (subtração), * (multiplicação), / (divisão)")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    while True:
        entrada = input("Digite a operação (ex: 2 + 3): ").strip()
        if entrada.lower() == "sair":
            print("Encerrando a calculadora. Até logo!")
            break
        try:
            # Aceita formatos como: 2 + 3, 4*5, 10 /2
            partes = entrada.replace(",", ".").split()
            if len(partes) == 3:
                num1, op, num2 = partes
            else:
                # Tenta separar por operador se não houver espaços
                for operador in ['+', '-', '*', '/']:
                    if operador in entrada:
                        num1, num2 = entrada.replace(",", ".").split(operador)
                        op = operador
                        break
                else:
                    print("Entrada inválida. Tente novamente.")
                    continue
            num1 = float(num1)
            num2 = float(num2)
            if op == "+":
                resultado = num1 + num2
            elif op == "-":
                resultado = num1 - num2
            elif op == "*":
                resultado = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = num1 / num2
            else:
                print("Operador inválido. Use +, -, * ou /.")
                continue
            print(f"Resultado: {resultado}\n")
        except Exception as e:
            print("Entrada inválida. Tente novamente.\n")

if __name__ == "__main__":
    calculadora()