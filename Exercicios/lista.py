#LISTAS
lista = ["Guitarra", "Bateria", "Violão"] # 0 1 e 2

#Incluir o valor no final da lista
lista.append(input("Digite o novo instrumento"))
print(lista)

#Incluir em um determinado item da lista um instrumento novo
lista.insert(0,"Violino")
print(lista)

#remover algum item - último item - pop()
lista.pop()
print(lista)

#remover algum item específico
#Não exclua um item que não existe dentro da lista
lista.remove("Bateria")
print(lista)

#Verificar a quantidade de itens na lista
print(len(lista))

#Existe algum item na lista mais de uma vez?
#Quantas vezes?
print(lista.count("Guitarra"))

#Ordenar uma lista em ordem alfabetica
lista.sort()
print(lista)

#Colocar na ordem invertida
lista.reverse()
print(lista)

