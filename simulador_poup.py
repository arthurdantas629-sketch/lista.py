#simulador de poupança--💰
aporte = float(input("quanto você vai depositar por mês?"))
juros = float(input("qual a taxa de juros atual da poupança?"))
meses = mt(input("por qual quantos meses você vai investir?"))
total = 0
for mes in range(1, meses +1):
    total = total + aporte
    total = total + (total*juros_decimal)
    print(f"mês{mes}:saldo total = R${total}")
print(f"Ao final de {meses}meses, você tera o valor de R$:{total:.2f}")