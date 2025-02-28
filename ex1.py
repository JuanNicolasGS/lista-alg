# 1. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool: até 20 litros, desconto de 3% por litro.
# acima de 20 litros, desconto de 5% por litro.
# Gasolina: até 20 litros, desconto de 4% por litro e acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def linhas():
    print("-" * 200)

def menu():
    linhas()
    print("MENU: ")
    print("A - Álcool - R$ 1,90")
    print("G - Gasolina - R$ 2,50")
    linhas()

def tabela_descontos():
    print("DESCONTOS:")
    print("3% - Álcool - até 20 litros")
    print("5% - Álcool - acima de 20 litros")
    print("4% - Gasolina - até 20 litros")
    print("6% - Gasolina - acima de 20 litros")
    linhas()

while True:
    menu()
    tabela_descontos()
    opcao = input("Escolha uma opção (P para parar): ").strip().upper()

    if opcao in ["A", "G"]:
        quantidade = float(input("Quantos litros: "))

        if opcao == "A":
            precoPorLitro = 1.90
            desconto = 0.03 if quantidade <= 20 else 0.05

        elif opcao == "G":
            precoPorLitro = 2.50
            desconto = 0.04 if quantidade <= 20 else 0.06

        preco_total = precoPorLitro * quantidade
        preco_com_desconto = preco_total * (1 - desconto)

        print(f"O custo com o desconto aplicado ficou: R$ {preco_com_desconto:.2f}")

    elif opcao == "P":
        print("Programa finalizado!")
        break
    else:
        print("OPÇÃO INVÁLIDA! Tente novamente.")