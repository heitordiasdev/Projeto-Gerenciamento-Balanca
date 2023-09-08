class ConfigEtiqueta:
    codigoInserido = None
    tamCodProd = None
    codPesavelInicio = None
    tipoVenda = None
    valido = None

    def __init__(self, tamCodProd, codPesavelInicio, tipoVenda, valido=False):

        if tamCodProd < 4 or tamCodProd > 6:
            raise ValueError("O tamanho do Código do produto deve estar entre 4 e 6!!")

        if codPesavelInicio < 1 or codPesavelInicio > 6:
            raise ValueError("O Código Verificador do início deve estar entre 1 e 6!!")

        if tipoVenda < 1 or tipoVenda > 2:
            raise ValueError("Tipo de venda deve ser 1 Peso ou 2 Preço!!")

        self.tamCodProd = tamCodProd
        self.codPesavelInicio = codPesavelInicio
        self.tipoVenda = tipoVenda
        self.valido = valido

    def inserirETratarCodigo(self, codigoInserido):

        self.codigoProd = []
        self.codPrecoPeso = []

        listCodigoInserido = []

        # transformar o codigo inserido em lista, para mostrar ao usuario cada saída dividida e correta
        for x in (str(codigoInserido)):
            digito = int(x)
            listCodigoInserido.append(digito)

        # print(self.codigoProd)
        # print(self.codPrecoPeso)
        if (int(listCodigoInserido[0]) == self.codPesavelInicio) and (len(listCodigoInserido) == 13):
            self.valido = True;
            for x, y in enumerate(listCodigoInserido):

                if 0 < x < 7:
                    self.codigoProd.append(y)

                if x >= 7:
                    self.codPrecoPeso.append(y)

            return [codigoInserido]
        else:
            return [self.valido, codigoInserido]

    def imprimirSaida(self):

        # transformar as duas listas em strings e depois inteiros
        self.codigoProd = int(''.join(map(str, self.codigoProd)))
        self.codPrecoPeso = int(''.join(map(str, self.codPrecoPeso)))

        self.codigoProd = f'{self.codigoProd:0{self.tamCodProd}}'

        if self.tipoVenda == 1:
            self.codPrecoPeso = self.codPrecoPeso / 1000
            saida = f'Código do produto: {self.codigoProd}\n' \
                    f'Codigo do produto pesável: {self.codPesavelInicio}\n' \
                    f'Peso do produto: {self.codPrecoPeso}'
        else:
            self.codPrecoPeso = self.codPrecoPeso / 1000
            self.codPrecoPeso = round(self.codPrecoPeso, 2)
            saida = f'Código do produto: {self.codigoProd}\n' \
                    f'Codigo do produto pesável: {self.codPesavelInicio}\n' \
                    f'Preço do produto: {self.codPrecoPeso}'

        return saida
