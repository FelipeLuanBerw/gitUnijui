import json 

usuarios = {'usuarios': [{'id': 1, 'nome': 'JoÃ£o Silva', 'email': 'joao@email.com', 'idade': 25}, {'id': 2, 'nome': 'Maria Souza', 'email': 'maria@email.com', 'idade': 30}]}

with open("text.json", 'w') as file:
    json.dump(usuarios, file)

def mostraDados(local):
    with open(local) as file:
        dados = json.load(file)
        print(json.dumps(dados, indent=4, sort_keys=True))
        
mostraDados("text.json")



