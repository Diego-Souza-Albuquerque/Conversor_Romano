
x = input("Digite um número para converter: ")
x = float(x)
x = int(x)
# Número até 3999
while x < 4000:
    x = str(x)
    tipo = len(x)

    def numerico(x):
        unidade = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        valor = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        posicao = valor.index(x)
        return unidade[posicao]

    def dezena(x):
        dezenas = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        valor = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]
        posicao = valor.index(x)
        return dezenas[posicao]

    def centena(x):
        centenas = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        valor = ["100", "200", "300", "400", "500", "600", "700", "800", "900"]
        posicao = valor.index(x)
        return centenas[posicao]

    def milhar(x):
        milhares = ["M", "MM", "MMM"]
        valor = ["1000", "2000", "3000"]
        posicao = valor.index(x)
        return milhares[posicao]

    if tipo == 1:
        numerico(x)
        num = numerico(x)
        print("Valor convertido:", num)

    if tipo == 2:
        y = x[0] + "0"
        z = x[1]
        dezena(y)
        dez = dezena(y)
        numerico(z)
        num = numerico(z)
        print("Valor convertido:", dez + num)

    if tipo == 3:
        k = x[0] + "00"
        y = x[1] + "0"
        z = x[2]
        dezena(y)
        dez = dezena(y)
        numerico(z)
        num = numerico(z)
        centena(k)
        cent = centena(k)
        print("Valor convertido:", cent + dez + num)

    if tipo == 4:
        k = x[0] + "000"
        y = x[1] + "00"
        z = x[2] + "0"
        w = x[3]
        dezena(z)
        dez = dezena(z)
        numerico(w)
        num = numerico(w)
        centena(y)
        cent = centena(y)
        milhar(k)
        mil = milhar(k)
        print("Valor convertido:", mil + cent + dez + num)

    x = input("\nDigite um novo número para converter: ")
    x = float(x)
    x = int(x)
