numero = 0
limite = 0

def testaImpares(numero):
    limite = numero + 1
    for i in range(2,numero,1):
        modulo = numero % i
        if modulo == 0:
            return False

    return True
    


def checaNumeroPrimo(numero):
    numero = int(input("Digite um número:"))
    modulo = numero % 2
    if modulo == 0 and numero > 2:
        print("O número não é primo!")
    elif testaImpares(numero) == False:
        print("O número não é primo!")
    else:
        print("O número é primo!")
        
checaNumeroPrimo(numero)