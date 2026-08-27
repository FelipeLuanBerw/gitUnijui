import json

pessoa = '{"nome": "Felipe", "linguagens" : ["Português", "Inglês"]}'

pessoa_dic = json.loads(pessoa)

print(pessoa_dic)

print(pessoa_dic['linguagens'])