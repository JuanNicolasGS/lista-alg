# 2. Desenvolva um programa que leia 2 números e em seguida pergunte ao usuário qual
# operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma
# frase que diga se o número é:

# • par ou ímpar;
# • positivo ou negativo;
# • inteiro ou decimal.
tipoNumero = ""

def linhas():
    print("-" * 50)

def menu():
    linhas()
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - PARA")
    linhas()

def calculo(primeiroNumero, segundoNumero, operacao):
    if operacao == "1":
        return primeiroNumero + segundoNumero
    elif operacao == "2":
        return primeiroNumero - segundoNumero
    elif operacao == "3":
        return primeiroNumero * segundoNumero
    elif operacao == "4":
        if segundoNumero == 0:
            print("Não é possível dividir por zero.")
            return None
        return primeiroNumero / segundoNumero
    else:
        print("Operação inválida!")
        return None
        
def frase(resultado):
    tipoNumero = ""
    
    if resultado % 2 == 0:
        tipoNumero = "par"
    else:
        tipoNumero = "ímpar"

    if resultado == 0:
        tipoNumero += ", neutro"
    elif resultado > 0:
        tipoNumero += ", positivo"
    else:
        tipoNumero += ", negativo"

    if resultado.is_integer():
        tipoNumero += " e inteiro"
    else:
        tipoNumero += " e decimal"    
    
    return tipoNumero

while True:
    menu()
    operacao = input("Qual operação você deseja realizar: ").strip()
    if operacao == "0":
        break
    
    primeiroNumero = float(input("Digite o primeiro número: "))
    segundoNumero = float(input("Digite o segundo número: "))


    resultado = calculo(primeiroNumero, segundoNumero, operacao)

    if resultado is not None:
        print(f"{resultado} é {frase(resultado)}")