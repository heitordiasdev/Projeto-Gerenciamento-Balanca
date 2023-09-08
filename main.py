from configBalanca.configEtiqueta import ConfigEtiqueta

matriz = [[],[]]

print("Bem vindo ao Software de Gerenciamento de Balanças\n")
print("Primeiramente, iremos realizar a configuração do Layout da Etiqueta!\n")

tamCodProduto = int(input('Qual o tamanho do código do produto? (Entre 4 e 6): '))
codProdPesavel = int(input('Qual o código do produto pesável? (1 e 6): '))
codPrecoPeso = int(input('Venda por Peso (1) ou Preço (2)? '))

partida = ConfigEtiqueta(tamCodProduto, codProdPesavel, codPrecoPeso)
codigo = int(input("Digite o código inteiro do produto que vc deseja inserir: "))
print("\n")

if partida.inserirETratarCodigo(codigo)[0] == False:
    matriz[1].append(partida.inserirETratarCodigo(codigo)[1])
    print("Codigo inválido!\n")

else:
    matriz[0].append(partida.inserirETratarCodigo(codigo))
    print(partida.imprimirSaida())

opcao = input("Deseja continuar inserindo o código PDV? 'S' OU 'N': ")
print("\n")

while opcao == 'S':

    partida = ConfigEtiqueta(tamCodProduto, codProdPesavel, codPrecoPeso)
    codigo = int(input("Digite o código inteiro do produto que vc deseja inserir: "))
    print("\n")


    if partida.inserirETratarCodigo(codigo)[0] == False:
        matriz[1].append(partida.inserirETratarCodigo(codigo)[1])
        print("Codigo inválido!\n")

    else:
        matriz[0].append(partida.inserirETratarCodigo(codigo))
        print(partida.imprimirSaida())

    opcao = input("Deseja continuar inserindo o código PDV? 'S' OU 'N': ")
    print("\n")

print(f'Matriz: {matriz}')