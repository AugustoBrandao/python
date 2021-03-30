#Função pra fazer as perguntas
#inserir no dicionario
def perguntar():
    return input("MENU: \n" + "<I>- Inserir Usuário \n" + "<P> Pesquisar um usuario \n" + "<E> Excluir Usuario\n" + "<L> Listar Usuário: ").upper()

#função base para inserir usuarios em uma lista
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Nome: ").upper(), input("Última data de acesso: "), input("Estação de acesso: ").upper()]

    salvar(dicionario)

#salvar o dicionario em um arquivo
#leitura e escrita
def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor)) 

