salario = float(input("Salário: "))

if salario < 0:        # : -> if == true
    salario = salario * -1
    print("Negativo")  # 4 espaços

print("Nome: {}  ||  Salário: {}".format(nome,salario))