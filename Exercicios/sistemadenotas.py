notas = []
opcao = -1

while opcao != 3:
    print(" 1-Notas: \n 2-Exibir notas: \n 3- Calcular a média \n 4-Sair")
    opcao = int(input("Escolha sua opcao: "))

    if opcao == 1 :
        notas.append(float(input("Digite a nota: ")))
    elif opcao == 2 :
        for x in notas: #Variavel X vai assumir cada um dos valores que existem dentro da lista de notas
            print(x)
        print(notas)
    #Calcular a média aritmética
    elif opcao == 3 :
        print(sum(notas) / len(notas))