# 4. Desenvolva um Programa que leia três números inteiros, em seguida mostre o maior e o
# menor deles.

c = 1
maior = 0
menor = 0

while c <= 3:
    num = int(input(f'Digite o {c}º número inteiro: '))
    if num > maior:
        maior = num
    else num < menor:
        menor = num
    c += 1