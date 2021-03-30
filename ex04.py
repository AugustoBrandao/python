#Desvio condicional aninhado
pontuacao = int(input("Pontos: "))

if pontuacao > 1000:
    print("3gb ")
else: 
    if pontuacao > 500:
        print("3gb ")
    else: 
        if pontuacao > 200:
            print("500mb ")
        else: 
            print("0")