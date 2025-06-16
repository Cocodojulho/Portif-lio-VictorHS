import random

pontuacao = 0
print("Nesse jogo você deverá responder apenas com a letra V ou a letra F")
varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->' ])
resposta = ''


def aumentar_pont1(pontuacao):
    pontuacao = pontuacao + 1
    return pontuacao
def aumentar_pont2(pontuacao):
    pontuacao +=2
    return pontuacao


def nivel1(varP, varQ, conectivo1, resposta, pontuacao ):
    print(f"P = {varP}")
    print(f"Q = {varQ}")
    print(f"P {conectivo1} Q")
    resposta = (input("Dificuldade I: V ou F?: ")).upper()

    if ((varP == "V" and varQ == "V") and conectivo1 == "^") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif((varP == "V" and varQ == "V") and conectivo1 == "^") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "V" and varQ == "V") and conectivo1 == "v") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif((varP == "V" and varQ == "V") and conectivo1 == "v") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "V" and varQ == "V") and conectivo1 == "-->") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif((varP == "V" and varQ == "V") and conectivo1 == "-->") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "V" and varQ == "F") and conectivo1 == "-->") and resposta == "F":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif((varP == "V" and varQ == "F") and conectivo1 == "-->") and resposta != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "V" and varQ == "F") and conectivo1 == "v") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "V" and varQ == "F") and conectivo1 == "v") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "V" and varQ == "F") and conectivo1 == "^") and resposta == "F":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "V" and varQ == "F") and conectivo1 == "^") and resposta != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "F" and varQ == "F") and conectivo1 == "^") and resposta == "F":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "F") and conectivo1 == "^") and resposta != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "F" and varQ == "F") and conectivo1 == "v") and resposta == "F":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "F") and conectivo1 == "v") and resposta != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    if ((varP == "F" and varQ == "F") and conectivo1 == "-->") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "F") and conectivo1 == "-->") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and conectivo1 == "-->") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "V") and conectivo1 == "-->") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and conectivo1 == "v") and resposta == "V":
        pontuacao=aumentar_pont1(pontuacao)


        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "V") and conectivo1 == "v") and resposta != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and conectivo1 == "^") and resposta == "F":
        pontuacao=aumentar_pont1(pontuacao)

        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((varP == "F" and varQ == "V") and conectivo1 == "^") and resposta != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    global total
    total = pontuacao
    print(f"Pontuação = {total}")
    return total




def nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, pontuacao):
    print(f"P = {varP}")
    print(f"Q = {varQ}")
    print(f"{negacao1}P {conectivo1} {negacao2}Q")
    resposta2 = (input("Difuculdade II: V ou F?: ")).upper()

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif (( varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    # só negação 1

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "^") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    # só negação 2

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    # ambas as negações

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "v") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "^") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "XOR") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "V" and varQ == "V") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "F":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif (( varP == "V" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "F":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")

    if ((varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 == "V":
        pontuacao = aumentar_pont2(pontuacao)
        print(f"Parabéns você acertou!\nsua pontuação é {pontuacao}")
    elif ((  varP == "F" and varQ == "F") and negacao1 == '~' and negacao2 == '~' and conectivo1 == "<-->") and resposta2 != "V":
        print(f"Que pena, não foi dessa vez.\nvocê tem {pontuacao} pontos")
    global total
    total = pontuacao
    return total


varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->'])
resposta = ''
nivel1(varP, varQ, conectivo1, resposta, pontuacao)
pepe = pontuacao
varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->'])
resposta = ''
nivel1(varP, varQ, conectivo1, resposta, total)
pepe = pontuacao
varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->'])
resposta = ''
nivel1(varP, varQ, conectivo1, resposta, total)
pepe = pontuacao
varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->'])
resposta = ''
nivel1(varP, varQ, conectivo1, resposta, total)
pepe = pontuacao
varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->'])
resposta = ''
nivel1(varP, varQ, conectivo1, resposta, total)


print("...Valendo o dobro de pontos ")

varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->', '<-->', 'XOR'])
negacao1 = random.choice([ '~', ''])
negacao2 = random.choice([ '~', ''])
nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, total)


varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->', '<-->', 'XOR'])
negacao1 = random.choice([ '~', ''])
negacao2 = random.choice([ '~', ''])
nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, total)


varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->', '<-->', 'XOR'])
negacao1 = random.choice([ '~', ''])
negacao2 = random.choice([ '~', ''])
nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, total)

varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->', '<-->', 'XOR'])
negacao1 = random.choice([ '~', ''])
negacao2 = random.choice([ '~', ''])
nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, total)

varP = random.choice(['V', 'F'])
varQ = random.choice(['V', 'F'])
conectivo1 = random.choice(['^', 'v', '-->', '<-->', 'XOR'])
negacao1 = random.choice([ '~', ''])
negacao2 = random.choice([ '~', ''])
nivel2(varP, varQ, conectivo1, negacao1, negacao2, resposta, total)
print(f"Você acertou {total} de 15 possíveis pontos!")
if 15 < total >= 8 :
    print("Exelente pontuação!")
elif total < 8:
    print("Você consegue mais!")
elif total == 15:
    print("Uauuu! Você acertou todas as questões, parabéns!!")