# 5. Desenvolva um programa que pede dois inteiro e armazene em duas variáveis. Em
# seguida, troque o valor das variáveis e exiba na tela: Trocar (inverter) valores de duas
# variáveis.

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
print(f"Antes de trocar: a = {a}, b = {b}")
a, b = b, a
print(f"Depois de trocar: a = {a}, b = {b}")