#Criando arquivo em json
import json
with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave,dados in dicionario.items():
        print(chave + " " + str(dados))

print(dicionario)

#Colocando dados no dicionario json
dicionario = {
    "CHAVES":["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO":["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "FLORINDA":["CHAVES DO 8", "14/04/2017", "RECEP_01"]
}

#criar dicionario e inserilo no arqui em json criado
with open("bd1.json", "w") as json_file
    json.dump(dicionario, "bd1.json") 