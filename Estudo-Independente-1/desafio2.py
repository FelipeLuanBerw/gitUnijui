produtos = {}


def recebeProdutos():

    global quantidadeProdutos

    quantidadeProdutos = int(input("Digite a quantidade de produtos:"))

    contador = 0

    while(contador < quantidadeProdutos):

        codigo = input("Digite o código do produto:")
        nome = input("Digite o nome do produto:")
        preco = float(input("Digite o preço do produto:"))
        quantidade = int(input("Digite a quantidade em estoque:"))

        produtos[codigo] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        print("")

        contador += 1


def consultaProduto(codigo):

    if codigo in produtos:

        produto = produtos[codigo]

        print("")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Quantidade em estoque: {produto['quantidade']}")

    else:

        print("")
        print("Produto não encontrado!")


def calculaValorEstoque():

    valorTotal = 0

    for codigo in produtos:

        produto = produtos[codigo]

        valorTotal += produto["preco"] * produto["quantidade"]

    return valorTotal


def calculaMaiorValor():

    maiorValor = 0
    nomeProduto = ""

    for codigo in produtos:

        produto = produtos[codigo]

        if produto["preco"] > maiorValor:

            maiorValor = produto["preco"]
            nomeProduto = produto["nome"]

    print("")
    print(f"O produto de maior valor unitário foi: {nomeProduto}")
    print(f"Valor: R$ {maiorValor}")


def navegar(navegador):

    match navegador:

        case 1:

            codigo = input("Digite o código do produto:")

            consultaProduto(codigo)

        case 2:

            valorEstoque = calculaValorEstoque()

            print("")
            print(f"O valor total do estoque é: R$ {valorEstoque}")

        case 3:

            calculaMaiorValor()

        case 4:

            return


def start():

    recebeProdutos()

    navegador = 0

    while navegador != 4:

        print("")
        print("Digite 1 para consultar um produto:")
        print("Digite 2 para calcular o valor total do estoque:")
        print("Digite 3 para identificar o produto de maior valor:")
        print("Digite 4 para sair!")

        navegador = int(input())

        navegar(navegador)


start()