conta = float(input("Digite o valor do conta: "))
saldo = float(input("Digite o valor do saldo: "))
debito = float(input("Digite o valor do debito: "))
credito = float(input("Digite o valor do credito: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print("Saldo positivo")
else:
    print("Saldo negativo")