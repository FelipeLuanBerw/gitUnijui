import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/andr3nf/clima_municipios_brasileiros/refs/heads/main/clima_historico_municipal.csv')

#___EXIBINDO NOMES DE TODAS AS COLUNAS___
#print(df.columns)

#___EXIBINDO TODOS OS DADOS___
#print(df) #Mostra todos os dados

#___VISUALIZAÇÃO PARCIAL DOS DADOS__
#df.head() #Mostra a primeira linha
#df.head(10) #Mostra as 10 primeiras linhas
#df.tail() #Mostra a última linhas
#df.tail(10) #Mostra as 10 últimas linhas
#df.iloc[20:30] #Mostra as linhas de 20 a 29
#df[["nome", "temperatura"]] #Mostra colunas específicas

#___EXIBINDO QUANTIDADE DE LINHAS E COLUNAS___
#print(df.shape) #Mostra a quantidade de linhas e colunas.

#___RENOMEANDO COLUNAS___
#df_renomeado = df.copy() # Criando uma cópia do DataFrame original
#df_renomeado = df_renomeado.rename(columns={ "nome": "municipio", "uf": "estado"}) # Renomeando algumas colunas

#___ADICIONANDO LINHAS___
#nova_linha = pd.DataFrame({"cod_ibge": [9999999], "nome_municipio": ["Município Teste"], "uf": ["RS"]}) # Criando uma nova linha
#df = pd.concat([df, nova_linha], ignore_index=True) # Adicionando a nova linha ao DataFrame

#___ADICIONANDO COLUNAS___
#df_coluna["exemplo"] = "teste" # Adicionando uma nova coluna - todas as linhas receberão o valor "teste"

#___DELETANDO LINHAS___
#df = df.drop(5) #Deletando a linha de índice 5

#___DELETANDO COLUNAS___
#df = df.drop("uf", axis=1) #Deletando uma coluna
#df = df(["uf", "periodo"], axis=1) #Deletando várias colunas

#___COMO MESCLAR DOIS DATAFRAMES___
#df_municipios = df.copy() #Criando uma cópia do dataframe original
#df_populacao = pd.DataFrame({"cod_ibge": [4300001, 4300002, 4300003],"populacao": [10000, 25000, 50000]}) # Criando um segundo DataFrame
#df_mesclado = pd.merge(df_municipios, df_populacao, on="cod_ibge") # Mesclando os dois DataFrames através do código IBGE

#___BUSCANDO DE FORMA CONDICIONAL___
#resultado = df[df["temp_media_jan"] > 25] 

#___AGRUPANDO RESULTADOS - "groupBy"___
#df_grupo.groupby("uf") - #Agrupa os resultados pela UF

#___CRIANDO UM DF ATRAVÉS DE UM DICIONÁRIO___
#dados = {"nome": ["João", "Maria", "Pedro"], "idade": [20, 25, 22], "nota": [8.5, 9.0, 7.5]} #Criando um dicionário
#df_dicionario = pd.DataFrame(dados) #Criando o DataFrame a partir do dicionário

#___DELETANDO lINHAS COM VALORES VAZIOS___
#df = df.dropna() #Para qualquer linha com um valor vazio.
#df = df.dropna(how="all") #Para remover linhas que todos os valores estão vazios
#df = df.dropna(subset=["idade", "nota"]) #Para remover linhas específicas com valores vazios

#___PREENCHENDO VALORES VAZIOS___
#df = df.fillna(0) #Preenche valores vazios com 0

#_________ATIVIDADE_________
#Buscando a cidade
cidade = df[df["nome_municipio"] == "Horizontina"] 

#Temperatura minima 
temperaturas = cidade[['tmin_jan',
       'tmin_fev', 'tmin_mar', 'tmin_abr', 'tmin_mai', 'tmin_jun', 'tmin_jul',
       'tmin_ago', 'tmin_set', 'tmin_out', 'tmin_nov', 'tmin_dez']]

temperatura_minima = temperaturas.min(axis=1).iloc[0]

#Défit hidríco
defHidrico = cidade[['def_jan',
       'def_fev', 'def_mar', 'def_abr', 'def_mai', 'def_jun', 'def_jul',
       'def_ago', 'def_set', 'def_out', 'def_nov', 'def_dez']]

maior_def = defHidrico.max(axis=1).iloc[0]

#Média das quatro estações
verao = cidade[["tmin_dez", "tmin_jan", "tmin_fev"]].mean(axis=1)
outono = cidade[["tmin_mar", "tmin_abr", "tmin_mai"]].mean(axis=1)
inverno = cidade[["tmin_jun", "tmin_jul", "tmin_ago"]].mean(axis=1)
primavera = cidade[["tmin_set", "tmin_out", "tmin_nov"]].mean(axis=1)

media = ((verao + outono + inverno + primavera) / 4).iloc[0]

print("Cidade = ", cidade)
print("")
print("Temperatura mínima = ", f"{temperatura_minima:.2f}")
print("Maior déficit hídrico = ", f"{maior_def:.2f}")
print("Temperatura média das estações = ", f"{media:.2f}")