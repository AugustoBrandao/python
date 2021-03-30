arquivo = open("primeiro_arquivo.txt", "w")

# r - read
# w - write
# a - leitura e gravação
# x - exclusivo - só você pode manipular 

with open("primeiro_arquivo.txt", "w") as arquivo:
    arquivo.write("\nBatata")

    #leitura do arquivo
    #abrir o arquivo em forma de leitura
with open("primeiro_arquivo.txt", "r") as arquivo:
    #for para executar a função de ler cada uma das linhas com 
    #a função redlines()
    for linha in arquivo.readlines():
        print(linha)