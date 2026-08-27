import json

with open('text.json', "r") as f:
    dados = json.load(f)
    
print(dados)

print(json.dumps(dados, indent=4, sort_keys=True))