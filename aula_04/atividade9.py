lado1 = float(input("Digite o valor do lado1: "))
lado2 = float(input("Digite o valor do lado2: "))
lado3 = float(input("Digite o valor do lado3: "))

if lado1 == lado2 == lado3:
    print ("Equilátero")
elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
    print ("Escaleno")
else:
    print ("Isoceles")

