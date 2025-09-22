# Descrição: Imagine que você é um mago que pode adivinhar
# o animal favorito das pessoas. Crie um programa
# que pergunte à pessoa se seu animal favorito é
# mamífero ou réptil. Se for mamífero, o programa deve
# sugerir que é um cachorro; se for réptil, o
# programa deve sugerir que é uma tartaruga.

animal = input("Seu animal favorito é um mamífero ou um réptil? ")

if animal == "reptil":
    print("Tartaruga")
else:
    print("Cachorro")

texto = "Qual seu animal favorito (m) ou (r):"
animal = input(texto).lower ()
#.lower ()vai retornar em minusculo

if animal == "m":
    print("Você gosta de doguinhos???")

elif animal == "r":
    print("Seu bicinho é tartaruga!!!")
else:
    print("Opção inválida!")

