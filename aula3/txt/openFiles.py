f = open("text.txt", "r")

conteudo = f.readlines()

#print(conteudo)

for linha in conteudo:
    print(linha)

f.close()
