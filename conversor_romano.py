
x = input("Digite um número para converter: ")
x = float(x)
x = int(x)

# Números até 3999
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

    if tipo == 1:  # condições para <= 9
        numerico(x)
        num = numerico(x)
        print("Valor convertido:", num)

    if tipo == 2:  # condições acima de 10 <= 99
        if x[1] == "0":
            dezena(x)
            dez = dezena(x)
            print("Valor convertido:", dez)
        else:
            y = x[0] + "0"
            z = x[1]
            dezena(y)
            dez = dezena(y)
            numerico(z)
            num = numerico(z)
            print("Valor convertido:", dez + num)

    if tipo == 3:  # condições acima de 100 <= 999
        if x[2] == "0":
            centena(x)
            cent = centena(x)
            print("Valor convertido:", cent)

        else:
            k = x[0] + "00"
            y = x[1] + "0"
            z = x[2]
            centena(k)
            cent = centena(k)
            dezena(y)
            dez = dezena(y)
            numerico(z)
            num = numerico(z)
            print("Valor convertido:", cent + dez + num)

    if tipo == 4:  # condições acima de 1000 <= 3999
        if x[3] == "0" and x[2] == "0" and x[1] == "0":
            milhar(x)
            mil = milhar(x)
            print("Valor convertido:", mil)

        elif x[3] == "0" and x[2] == "0":
            k = x[0] + "000"
            y = x[1] + "00"
            milhar(k)
            mil = milhar(k)
            centena(y)
            cent = centena(y)
            print("Valor convertido:", mil + cent)

        elif x[3] == "0":
            k = x[0] + "000"
            y = x[1] + "00"
            z = x[2] + "0"
            milhar(k)
            mil = milhar(k)
            centena(y)
            cent = centena(y)
            dezena(z)
            dez = dezena(z)
            print("Valor convertido:", mil + cent)

        else:
            k = x[0] + "000"
            y = x[1] + "00"
            z = x[2] + "0"
            w = x[3]
            milhar(k)
            mil = milhar(k)
            centena(y)
            cent = centena(y)
            dezena(z)
            dez = dezena(z)
            numerico(w)
            num = numerico(w)
            print("Valor convertido:", mil + cent + dez + num)

    x = input("\nDigite um novo número para converter: ")
    x = float(x)
    x = int(x)

print("PROGRAMA FINALIZADO")
