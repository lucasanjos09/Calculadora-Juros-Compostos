depositoinicial = float(input("Digite o valor do deposito inicial: "))
juros = float(input("Digite o valor da taxa de juros: "))
mensal = float(input("Digite o valor a ser depositado mensalmente: "))
n = int(input("Digite o número de meses: "))
meses = 1 
deposito = depositoinicial
while meses <= n :
    
    deposito = mensal + (deposito * (1 + juros/100))
    meses = meses + 1
total = depositoinicial + (mensal * (n - 1) )
print("O valor total é",deposito)
print("O total investido é:",total)
print("O seu lucro é: ",deposito - total)