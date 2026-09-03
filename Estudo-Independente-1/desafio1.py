estudantes = []
notas = []


def recebeEstudantes() :
    global quantidadeEstudantes
    quantidadeEstudantes = int (input("Digite a quantidade de estudantes:"))
    
    contador = 0
    while(contador < (quantidadeEstudantes)) :
        estudantes.append(input("Digite o nome do aluno:"))
        notas.append(float(input("Digite a nota do aluno:")))
        print("")
        contador += 1
    
def calculaMaiorNota(notas):
    maiorNota = 0
    for nota in notas:
        if nota > maiorNota:
            maiorNota = nota
    return maiorNota

def calculaMenorNota(notas):
    menorNota = 11
    for nota in notas:
        if nota < menorNota:
            menorNota = nota
    return menorNota

def calculaMedia(notas, quantidadeEstudantes):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / quantidadeEstudantes
    return media
    
def calculaAprovados(quantidadeEstudantes, notas): 
    aprovados = []
    for i in range(0, quantidadeEstudantes, 1):
        if notas[i] >= 6:
            aprovados.append(i)
    return aprovados

def calculaReprovados(quantidadeEstudantes, notas): 
    reprovados = []
    for i in range(0, quantidadeEstudantes, 1):
        if notas[i] < 6:
            reprovados.append(i)
    return reprovados

def navegar(navegador):
    match navegador:
                case 1:
                    menor = calculaMenorNota(notas)
                    print("")
                    print(f"A menor nota foi: {menor}")
                case 2:
                    maior = calculaMaiorNota(notas)
                    print("")
                    print(f"A maior nota foi: {maior}")
                case 3:
                    media = calculaMedia(notas, quantidadeEstudantes)
                    print("")
                    print(f"A média da turma foi: {media}")
                case 4:
                    aprovados = calculaAprovados(quantidadeEstudantes, notas)   
                    nomesAprovados = []
                    for aprovado in aprovados:
                        nomesAprovados.append(estudantes[aprovado])
                    print("")
                    print(f"A turma teve {len(nomesAprovados)} aprovados!")
                    print(f"Os aprovados foram: {nomesAprovados}")
                case 5:
                    reprovados = calculaReprovados(quantidadeEstudantes, notas)   
                    nomesReprovados = []
                    for reprovado in reprovados:
                        nomesReprovados.append(estudantes[reprovado])
                    print("")
                    print(f"A turma teve {len(nomesReprovados)} reprovados!")
                    print(f"Os reprovados foram: {nomesReprovados}")
                case 9: 
                    return

def start():
    recebeEstudantes()
    navegador = 0
    while navegador != 6:
        print("")
        print("Digite 1 para calcular a menor nota:")
        print("Digite 2 para calcular a maior nota:")
        print("Digite 3 para calcular a media da turma:")
        print("Digite 4 para calcular os estudanets aprovados:")
        print("Digite 5 para calcular os estudantes reprovados:")
        print("Digite 6 para sair!")
        navegador = int(input())
        navegar(navegador)
        
start()