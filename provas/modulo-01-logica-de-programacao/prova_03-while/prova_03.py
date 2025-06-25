tentativa = 0
numero_adivinhar = 7

while True:
    tentativa += 1
    numero_usuario = int(
        input("Digite um numero para tentar acertar o numero escolhido\n"))

    if numero_usuario == numero_adivinhar:
        print("Parabens você acertou o numero!!!!")
        break

    elif tentativa == 3:
        print("Que pena vc não conseguiu acertar o numero nas tres tentivas disponiveis, quem sabe vc tenha mais sorte na proxima")
        break

    else:
        print("Esse não e o numero certo, tente novamente!!!")
