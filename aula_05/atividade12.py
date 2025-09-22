# Descrição: Um guerreiro precisa de uma armadura especial para a batalha.
# Para forjar a armadura, ele precisa de uma liga metálica que combina ferro e ouro.
# O ferreiro diz que a liga precisa ter no mínimo 70% de ferro.
# Crie um programa que receba a quantidade de ferro e ouro em kg e verifique se
# a porcentagem de ferro na liga é suficiente.

ouro = input("Digite a quantidade de ouro: ")
ferro = input("Digite a quantidade de ferro: ")

ouro = float(ouro)
ferro = float(ferro)

proporcao_ferro = ferro / (ouro + ferro)

if proporcao_ferro >= 7:
    print(f'A Proposrção de Ferro na liga é de: {proporcao_ferro:.2f}')
    print("Será possível criar a armadura de Pagasus")
else:
    print("Quantidade de Ferro insuficiente")
    print(f"Proporção de ferro é apenas: {proporcao_ferro:.2f}")



