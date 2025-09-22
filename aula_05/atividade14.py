# Um colecionador de moedas tem 3 tipos de moedas:
# de 1 real, de 50 centavos e de 25 centavos.
# Escreva um programa que receba a quantidade de cada
# tipo de moeda e calcule o valor total que o colecionador
# tem.

moeda1 = int(input("Digite a quantidade de R$1,00: "))
moeda2 = int(input("Digite a quantidade de R$0,50: "))
moeda3 = int(input("Digite a quantidade de R$0,25: "))

valor1 = moeda * 1
valor2 = moeda2 * 0,50
valor3 = moeda3 * 0,25

valor_total = valor1 + valor2 + valor3

print(f'O Total em reais é de R$ {valor_total}')

