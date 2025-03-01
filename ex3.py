# 3. Desenvolva um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é
# descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
# de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas
# conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS ( 10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00

salarioBruto = float(input("Digite seu salario bruto para calcular os decontos: "))
IR = 0
salarioLiquido = 0
INSS = salarioBruto * 0.10
FGTS = salarioBruto * 0.11
totalDescontos = 0
if salarioBruto <= 900:
    IR = salarioBruto * 0
    totalDecontos = INSS
    salarioLiquido = salarioBruto - totalDescontos
    print(f"Salario bruto: R$ {salarioBruto}\n(INSENTO) IR: R$ 0.00\n(-) INSS (10%): R$ {INSS}\nFGTS (11%): R$ {FGTS}\nTotal de descontos: R$ {totalDescontos}\nSalario Liquido: R$ {salarioLiquido}")

elif salarioBruto > 900 and salarioBruto <= 1500:
    IR = salarioBruto * 0.05
    totalDescontos = INSS + IR
    salarioLiquido = salarioBruto - totalDescontos
    print(f"Salario bruto: R$ {salarioBruto}\n(-) IR (5%): R$ {IR}\n(-) INSS (10%): R$ {INSS}\nFGTS (11%): R$ {FGTS}\nTotal de descontos: R$ {totalDescontos}\nSalario Liquido: R$ {salarioLiquido}")
    
elif salarioBruto > 1500 and salarioBruto <= 2500:
    IR = salarioBruto * 0.10
    totalDescontos = INSS + IR
    salarioLiquido = salarioBruto - totalDescontos
    print(f"Salario bruto: R$ {salarioBruto}\n(-) IR (10%): R$ {IR}\n(-) INSS (10%): R$ {INSS}\nFGTS (11%): R$ {FGTS}\nTotal de descontos: R$ {totalDescontos}\nSalario Liquido: R$ {salarioLiquido}")

else:
    IR = salarioBruto * 0.20
    totalDescontos = INSS + IR
    salarioLiquido = salarioBruto - totalDescontos
    print(f"Salario bruto: R$ {salarioBruto}\n(-) IR (20%): R$ {IR}\n(-) INSS (10%): R$ {INSS}\nFGTS (11%): R$ {FGTS}\nTotal de descontos: R$ {totalDescontos}\nSalario Liquido: R$ {salarioLiquido}")