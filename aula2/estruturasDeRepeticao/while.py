senha = "214365"
digitado = " ";
while (digitado != senha):
    digitado = input("Digite sua senha:")
    if digitado == senha :
        print("Acesso liberado!")
    else: 
        print("Acesso negado, tente novamente!")