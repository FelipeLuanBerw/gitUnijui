import json

import requests

pessoa = '{"nome": "Felipe", "linguagens" : ["Português", "Inglês"]}'

pessoa_dic = json.loads(pessoa)

pessoa_add = {"casado" : True, "idade" : 32}

pessoa_dic.update(pessoa_add)

with open("pessoa.json","w") as json_file:
    json.dump(pessoa_dic, json_file) 
    
#print(json.dumps(pessoa_dic, indent=4, sort_keys=True, separators=(' , ',' : ')))

resposta = requests.get("https://api.randomuser.me")

#print(resposta.status_code)

#print(resposta.text)

dados = json.loads(resposta.text)
#print(dados)

print(json.dumps(dados, indent=4, sort_keys= True))