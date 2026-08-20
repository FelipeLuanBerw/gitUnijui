nota = float (input("Digite o valor da nota:"))
if nota < 60: 
    print("Sua nota {} foi insuficiente".format(nota))
elif nota > 60 and nota < 70:
    print("você está em recuperação")
else: 
    print("Você está aprovado!")
    print("Nota boa!")

