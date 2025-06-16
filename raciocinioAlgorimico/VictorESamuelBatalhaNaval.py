import random
import copy
import time
import colorama
from colorama import init, Fore, Back, Style
init()
reiniciar = True
while reiniciar: #utilizado para reinicar ou parar no final do jogo
    possiveisAtaquesIAx = [] #lista com possiveis opções da IA
    possiveisAtaquesIAy = [] #lista com possiveis opções da IA
    listaLetras = ['-', '  a', '  b', '  c', '  d', '  e', '  f', '  g', '  h', '  i', '  j', '  k', '  l', '  m',
                   '  n', '  o', '  p', '  q', '  r', '  s', '  t'] #Lista para mostrar as letras na matriz
    condicoes = False #Condições para o while inicial que pega modo altura e largura
    contador = 0

    print("Atenção, você só pode jogar com um numero de casas entre 10x10 e 20x20")
    while condicoes == False:  # Loop até as condições iniciais forem completadas.
        altura = input("Quantas casas você quer que o jogo tenha de altura?")
        largura = input("Quantas casas você quer que o jogo tenha de largura?")
        modo = input(
            "Qual modo de jogo você escolhe?\n1 - Jogador 1 vs Jogador 2\n2 - Jogador 1 vs Inteligência Artificial\n(Digite um número)")
        if altura.isdigit() == False or largura.isdigit() == False or modo.isdigit() == False:
            print("Algum valor foi digitado inadequadamente, tente novamente:")
            continue
        else:
            altura = int(altura)
            largura = int(largura)
            modo = int(modo)
        if modo != 1 and modo != 2:
            print("Opção inválida, tente novamente!")
            continue
        batalhaNaval = [[]]
        if (altura > 20 or largura > 20 or altura < 10 or largura < 10) == False:
            altura = altura + 1  # coloquei +1
            largura = largura + 1  # coloquei +1
            condicoes = True
        else:
            print("Você só poder jogar com um número de casas entre 10x10 e 20x20, tente novamente.")
        # Altura e Largura já definidos. obs: a largura e altura são 1 casas maior que o input pois vai considerar o display das letras e números que estão só para auxilio no jogo


    def mostrarmatriz(matriz): #Função para mostrar matriz(com cor dependendo a situação)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == '[~]':
                    print(f"{Fore.BLUE}{matriz[i][j]}{Style.RESET_ALL}", end=' ')
                elif matriz[i][j] == '[O]':
                    print(f"{Fore.RED}{matriz[i][j]}{Style.RESET_ALL}", end=' ')
                elif matriz[i][j] == '[X]':
                    print(f"{Fore.GREEN}{matriz[i][j]}{Style.RESET_ALL}", end=' ')
                else:
                    print(matriz[i][j], end=' ')
            print()
        return matriz


    def letrasPraNumeros(cordLetra):
        mapa = {letra: i for i, letra in enumerate("abcdefghijklmnopqrst", 1)}
        return mapa.get(cordLetra.lower(), 0)


    def batalhaNaval1(alt, larg, cont): #função para já fazer com que a o tabuleiro fique com as letras e números extras digitados
        batalhaNaval = [['[~]' for a in range(larg)] for a in range(altura)]  # tirei +1
        for linhasNumeros in range(len(batalhaNaval)):
            if cont < 10:
                batalhaNaval[linhasNumeros][0] = f"{cont} "
            else:
                batalhaNaval[linhasNumeros][0] = cont
            cont = cont + 1
            for colunasLetras in range(len(batalhaNaval[linhasNumeros])):
                batalhaNaval[0][colunasLetras] = listaLetras[colunasLetras]

        mostrarmatriz(batalhaNaval)
        return batalhaNaval


    def criarBarco(alt, larg, batalhNvl, casas, nome, jogador, gameMode):#cria os barcos
        if modo != 2 or jogador != "jogador2":#só aparece se o jogador não for IA.
            print(f"Vez do {jogador}!")
            print("Atenção, se você digitar alguma coisa diferente das letras ou números do jogo, sua letra ou número será definida automaticamente, portanto é necessário ter cautela")
        canPlace = False #condição para while, enquanto for impossível de colocar não vai colocar o barco
        cords = 0
        while canPlace == False:
            interceptador = 0 # váriavel que será aumentada quando a posição de dois barcos forem interceptadas
            if gameMode == 1 or jogador == "jogador1":  #só aparece se o jogador não for IA.
                letraCoordenada = input(f"Digite uma letra como a primeira coordenada do {nome} (que tem {casas} casas): ") #pega a letra
                letraCoordenada = letraCoordenada.lower() #transforma para minúscula
                numletra = letrasPraNumeros(letraCoordenada) #cria váriavel que pega o número da letra
            elif gameMode == 2 and jogador == "jogador2":
                numletra = (random.randint(1, (larg - 1)))  # larg -1 pois larg está como 21 (incluindo a parte não jogavel da matriz(os números))
            if numletra < 1:
                numletra = 1  # se o jogador jogar um número menor que 1, será escolhido o número 1
            elif numletra > (larg - 1): #se o número(letra nesse caso) for maior do que o disponivel no jogo a coordenada vai na ultima coluna
                numletra = (larg - 1)
            if gameMode == 1 or jogador == "jogador1": #Excluí IA
                numeroCoordenada = input(f"Digite um número como a primeira coordenada do {nome} (que tem {casas} casas): ")
                if numeroCoordenada.isdigit(): #verifica se é número
                    numeroCoordenada = int(numeroCoordenada) #se for transforma em int
                else:
                    print("Ocorreu um erro! Reiniciando a escolha de casa.") #volta ao começo do loop
                    continue
            elif gameMode == 2 and jogador == "jogador2": #só IA
                numeroCoordenada = (random.randint(1, (alt - 1)))
            if numeroCoordenada < 1:
                numeroCoordenada = 1
            elif numeroCoordenada > (alt - 1):
                numeroCoordenada = (alt - 1)

            if batalhNvl[numeroCoordenada][numletra] != '[~]': #Se já esta selcionado retorna ao início do loop
                if gameMode != 2 or jogador != "jogador2":
                    print("Valor já esta em uso, tente novamente!")
                continue
            if gameMode == 1 or jogador == "jogador1":
                direcaoCoordenada = input("Digite a direção do seu barco 'vertical' ou 'horizontal'")
            elif gameMode == 2 and jogador == "jogador2":
                direcaoCoordenada = random.choice(['vertical', 'horizontal'])
            if numeroCoordenada <= (alt - casas) and direcaoCoordenada == 'vertical':# se a direção é vertical e o numero da cordenada é menor ou igual a (altura)-(casas do barco) para evitar problemas de index out of range
                for partesNaviosY in range(casas):
                    if batalhNvl[numeroCoordenada + partesNaviosY][numletra] == '[N]': #Verifica se os próximos números pra baixo são '[N]' se for inteceptador+=1
                        interceptador += 1
            elif numeroCoordenada > (alt - casas) and direcaoCoordenada == 'vertical':#Ainda se o numero de cordenada é maior que altura-casas ele verifica os valores
                for partesNaviosY in range(alt - numeroCoordenada):#alt-numeroCoordenada é o limite para não dar index out of range
                    if batalhNvl[numeroCoordenada + partesNaviosY][numletra] == '[N]':
                        interceptador += 1
            if numletra <= (larg - casas) and direcaoCoordenada == 'horizontal':#mesma coisa que o vertical só que agora com o horizontal
                for partesNaviosX in range(casas):
                    if batalhNvl[numeroCoordenada][numletra + partesNaviosX] == '[N]':
                        interceptador += 1
            elif numletra > (larg - casas) and direcaoCoordenada == 'horizontal':
                for partesNaviosX in range(larg - numletra):
                    if batalhNvl[numeroCoordenada][(numletra + partesNaviosX)] == '[N]':
                        interceptador += 1
            if interceptador > 0: #se interceptador for maior que 0 vai mostrar uma mensagem e retornar ao início do loop
                if modo != 2 or jogador != "jogador2":
                    print("Navio já se encontra nessa coordenada, tente novamente!")
                continue
            if direcaoCoordenada != 'vertical' and direcaoCoordenada != 'horizontal':
                print("Valor inválido, tente novamente.")
                continue
            elif direcaoCoordenada == 'horizontal' and (numletra + casas) > larg:  #se o numletra + casas ultrapassar a largura, volta ao começo
                if modo != 2 or jogador != "jogador2":
                    print(f"Valor ultrapassa do limite de números, tente no máximo {casas} letras antes do limite")
                continue
            elif direcaoCoordenada == 'vertical' and (numeroCoordenada + casas) > altura:  #se o numCoordenada + casas ultrapassar a largura, volta ao começo
                if modo != 2 or jogador != "jogador2":
                    print(
                        f"Valor ultrapassa do limite de números, tente no máximo {casas} números antes do limite (tente na casa {alt - casas})")
                continue
            else:
                canPlace = True #já pode sair do loop
                batalhNvl[numeroCoordenada][numletra] = '[N]' #coloca o primeiro '[N]'
                if direcaoCoordenada == 'vertical':
                    for i in range(casas):
                        batalhNvl[numeroCoordenada + i][numletra] = '[N]'#coloca os outros '[N]' na vertical
                elif direcaoCoordenada == 'horizontal':
                    for j in range(casas):
                        batalhNvl[numeroCoordenada][numletra + j] = '[N]'#coloca os outros '[N]' na horizontal
                # para printar a matriz
                if modo == 1 or (modo == 2 and jogador == "jogador1"):#não pergunta se quer ver a matriz para IA
                    mostrarMatriz = input("Quer ver a matriz? 'sim' ou 'nao'")
                else:
                    mostrarMatriz = "nao"
                if mostrarMatriz == "sim":
                    mostrarmatriz(batalhNvl)
                else:
                    print()

        return batalhNvl #retorna os barcos posicionados na matriz


    def jogada(alt, larg, batalhNvlBarcos, batalhNvlAtaques, jogador, gameMode, pontos, batalhNvlOriginal):#jogada(palpites) de casas uma por uma
        ataquePossivel = False
        while ataquePossivel == False:
            print("\n\n\n\n\n\n")
            displayAtaques = copy.deepcopy(batalhNvlAtaques) #copia o batalha naval ataques(que é o que tem a posição dos barcos do oponente) para mostrar o jogo ao jogador
            for i in range(len(displayAtaques)):
                for j in range(len(displayAtaques[i])):
                    if displayAtaques[i][j] == '[N]':
                        displayAtaques[i][j] = '[~]'
            mostrarmatriz(displayAtaques)
            print(f"Jogada do {jogador} que tem {pontos} pontos")
            if modo == 1 or (modo == 2 and jogador == "jogador1"):#sem IA
                palpiteLetra = input("Digite uma letra que esteja no jogo: ")
                palpiteLetra = palpiteLetra.lower()
                palpiteCordX = letrasPraNumeros(palpiteLetra)
            else:#com IA
                IAdecision = random.choice(['Estratégica', 'Estratégica', 'Estratégica', 'Aleatória']) #Estratégica: verifica as casas ao redor e se tiver [N] por perto ele escolhe aleatóriamente jogar em alguma casa ao redor
                IAstrategyXY = random.choice(['X', 'Y']) #se vai jogar em uma casa pra cima ou baixo(Y) ou aos lados(X)
                if IAdecision == 'Estratégica':
                    possiveisAtaquesIAx = []#reseta as listas
                    possiveisAtaquesIAy = []
                    for i in range(len(batalhNvlBarcos)):
                        for j in range(len(batalhNvlBarcos[i])):
                            if (j + 1) >= larg:  # Adicionado porque deu erro ao verificar batalhNvlBarcos list index out of range
                                if batalhNvlAtaques[i][j] == '[X]' and batalhNvlBarcos[i][j - 1] == "[N]":
                                    possiveisAtaquesIAx.append(j - 1)#adiciona um possível ataque x e y
                                    possiveisAtaquesIAy.append(i)
                            elif batalhNvlAtaques[i][j] == '[X]' and (batalhNvlBarcos[i][j - 1] == "[N]" or batalhNvlBarcos[i][j + 1] == "[N]"):
                                if (j - 1) > 0:
                                    possiveisAtaquesIAx.append(j - 1)#adiciona um possível ataque x e y(só se j-1 for maior que 0
                                    possiveisAtaquesIAy.append(i)
                                if (j + 1) < larg:
                                    possiveisAtaquesIAx.append(j + 1)#adiciona um possível ataque x e y(só se (j+1) for menor que larg
                                    possiveisAtaquesIAy.append(i)
                    if len(possiveisAtaquesIAx) > 0 and IAstrategyXY == 'X': #se tiver possiveis ataques disponíveis e for escolhido atacar aos lados
                        indiceListaCords = random.randint(0, len(possiveisAtaquesIAx) - 1)#escolhe aleatoriamente um possivel ataque
                        palpiteCordX = possiveisAtaquesIAx[indiceListaCords]
                        jogadaCalculadaX = True#utilizado para escolher corretamente o elemento certo da jogadaCalculdaY depois
                    else:
                        palpiteCordX = (random.randint(1, (larg - 1)))
                        jogadaCalculadaX = False
                else:
                    palpiteCordX = (random.randint(1, (larg - 1)))
                    jogadaCalculadaX = False
            if palpiteCordX < 1:
                if modo == 1 or (modo == 2 and jogador == "jogador1"):
                    print("Letra inexistente no jogo")
                continue
            if palpiteCordX > (larg - 1):
                if modo == 1 or (modo == 2 and jogador == "jogador1"):
                    print("Letra inexistente no jogo")
                continue
            if modo == 1 or (modo == 2 and jogador == "jogador1"):
                palpiteCordY = input("Digite um número que esteja no jogo: ")#pegar a coordenada Y(número)
                if palpiteCordY.isdigit():
                    palpiteCordY = int(palpiteCordY)  # Verificação para ficar melhor.
                else:
                    print("\nNão foi digitado um número, tente novamente!")
                    continue
            else:
                if jogadaCalculadaX == True:#se foi definida uma jogadaCalculadaX em certo local ele vai pegar a altura certa daquela jogada.
                    if len(possiveisAtaquesIAy) > 0:
                        palpiteCordY = possiveisAtaquesIAy[indiceListaCords]
                elif jogadaCalculadaX == False and IAdecision == 'Estratégica': #Se não deu certo jogadaCalculadaX, e a decisão é estratégica, ela procura jogar acima ou abaixo de um acerto
                    for i in range(len(batalhNvlBarcos)):
                        for j in range(len(batalhNvlBarcos[i])):
                            if (i + 1) >= larg:
                                if batalhNvlAtaques[i][j] == '[X]' and batalhNvlBarcos[i - 1][j] == "[N]":
                                    possiveisAtaquesIAy.append(i - 1)
                                    possiveisAtaquesIAx.append(j)
                            elif batalhNvlAtaques[i][j] == '[X]' and (
                                    batalhNvlBarcos[i + 1][j] == "[N]" or batalhNvlBarcos[i - 1][j] == "[N]"):
                                if (i - 1) > 0:
                                    possiveisAtaquesIAy.append(i - 1)
                                    possiveisAtaquesIAx.append(j)
                                if (i + 1) < larg:
                                    possiveisAtaquesIAy.append(i + 1)
                                    possiveisAtaquesIAx.append(j)
                    if len(possiveisAtaquesIAy) > 0 and IAstrategyXY == 'Y':
                        indexListaCords2 = random.randint(0, len(possiveisAtaquesIAy) - 1)
                        palpiteCordY = possiveisAtaquesIAy[indexListaCords2]
                        palpiteCordX = possiveisAtaquesIAx[indexListaCords2]#redefine palpiteCordX para ficar na posição X correta em relação a Y
                    else:
                        palpiteCordY = (random.randint(1, (larg - 1)))
                else:
                    palpiteCordY = (random.randint(1, (larg - 1)))

            if palpiteCordY < 1:#Verificação
                if modo == 1 or (modo == 2 and jogador == "jogador1"):
                    print("Digite um número maior que 0")
                continue
            if palpiteCordY > (alt - 1):
                if modo == 1 or (modo == 2 and jogador == "jogador1"):
                    print("Digite um número menor")
                continue
            if batalhNvlAtaques[palpiteCordY][palpiteCordX] == '[O]' or batalhNvlAtaques[palpiteCordY][palpiteCordX] == '[X]':
                if modo == 1 or (modo == 2 and jogador == "jogador1"):
                    print("Você já atacou este lugar, tente novamente.")
                continue
            ataquePossivel = True
            #verifica se acertou ou não batlhNvlBarcos vai ser a sua matriz e
            if batalhNvlBarcos[palpiteCordY][palpiteCordX] == '[N]':
                batalhNvlAtaques[palpiteCordY][palpiteCordX] = '[X]'
                print("Jogador acertou!")
                pontos += 1
            elif batalhNvlBarcos[palpiteCordY][palpiteCordX] == '[~]':
                batalhNvlAtaques[palpiteCordY][palpiteCordX] = '[O]'
                print("Jogador errou!")
            displayAtaques = copy.deepcopy(batalhNvlAtaques) #cópia para mostrar sem nenhum [N] os acertos e erros do jogador
            for i in range(len(displayAtaques)):
                for j in range(len(displayAtaques[i])):
                    if displayAtaques[i][j] == '[N]':
                        displayAtaques[i][j] = '[~]'
            mostrarmatriz(displayAtaques)
            print(f"{jogador} tem {pontos} pontos")
            return batalhNvlAtaques, pontos

    #função que repete a função jogada até dar 19 pontos(quantidade total de casas)
    def jogadas(pontjogadorA, pontjogadorB):
        listaAtualizada1, Jogador1Pontos = jogada(altura, largura, tabuleiroAtualizado2, tabuleiroAtualizado1copy,"jogador1", modo, pontjogadorA, batalhaNavalDisplay)
        time.sleep(2)
        listaAtualizada2, Jogador2Pontos = jogada(altura, largura, tabuleiroAtualizado1, tabuleiroAtualizado2copy,"jogador2", modo, pontjogadorB, batalhaNavalDisplay)
        time.sleep(2)
        while Jogador1Pontos < 19 and Jogador2Pontos < 19:
            listaAtualizada1, Jogador1Pontos = jogada(altura, largura, tabuleiroAtualizado2, listaAtualizada1,"jogador1", modo, Jogador1Pontos, batalhaNavalDisplay)
            time.sleep(2)
            if Jogador1Pontos < 19:
                listaAtualizada2, Jogador2Pontos = jogada(altura, largura, tabuleiroAtualizado1, listaAtualizada2,"jogador2", modo, Jogador2Pontos, batalhaNavalDisplay)
                time.sleep(2)
            if Jogador1Pontos == 19:
                print("Parabéns, o jogador 1 venceu!!!")
            if Jogador2Pontos == 19:
                print("Parabéns, o jogador 2 venceu!!!")

        return listaAtualizada1, listaAtualizada2


    def pegarHistDeJogo(jogofinalmatriz, tirostotais, tiroserrados, tirosacertados, ganhou): #pega o historico para colocar em pasta txt
        for i in range(len(jogofinalmatriz)):
            for j in range(len(jogofinalmatriz)):
                if jogofinalmatriz[i][j] == '[O]':
                    tirostotais += 1
                    tiroserrados += 1
                elif jogofinalmatriz[i][j] == '[X]':
                    tirostotais += 1
                    tirosacertados += 1
                if tirostotais == 19:
                    ganhou = True
        return tirostotais, tiroserrados, tirosacertados, ganhou

    #jogo através das funções:
    batalhaNaval = batalhaNaval1(altura, largura, 0)  # Usa a função batalha naval e usa a altura e largura.
    tabuleiroAtualizado1 = criarBarco(altura, largura, batalhaNaval, 4, 'Porta-Aviões', "jogador1", modo)
    tabuleiroAtualizado1 = criarBarco(altura, largura, tabuleiroAtualizado1, 5, 'Encouraçado ', "jogador1", modo)
    tabuleiroAtualizado1 = criarBarco(altura, largura, tabuleiroAtualizado1, 3, 'Contratorpedeiro', "jogador1", modo)
    tabuleiroAtualizado1 = criarBarco(altura, largura, tabuleiroAtualizado1, 3, 'Contratorpedeiro', "jogador1", modo)
    tabuleiroAtualizado1 = criarBarco(altura, largura, tabuleiroAtualizado1, 2, 'Submarino', "jogador1", modo)
    tabuleiroAtualizado1 = criarBarco(altura, largura, tabuleiroAtualizado1, 2, 'Submarino', "jogador1", modo)

    tabuleiroAtualizado1copy = copy.deepcopy(tabuleiroAtualizado1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    batalhaNaval2 = batalhaNaval1(altura, largura, 0)
    tabuleiroAtualizado2 = criarBarco(altura, largura, batalhaNaval2, 4, 'Porta-Aviões', "jogador2", modo)
    tabuleiroAtualizado2 = criarBarco(altura, largura, tabuleiroAtualizado2, 5, 'Encouraçado ', "jogador2", modo)
    tabuleiroAtualizado2 = criarBarco(altura, largura, tabuleiroAtualizado2, 3, 'Contratorpedeiro', "jogador2", modo)
    tabuleiroAtualizado2 = criarBarco(altura, largura, tabuleiroAtualizado2, 3, 'Contratorpedeiro', "jogador2", modo)
    tabuleiroAtualizado2 = criarBarco(altura, largura, tabuleiroAtualizado2, 2, 'Submarino', "jogador2", modo)
    tabuleiroAtualizado2 = criarBarco(altura, largura, tabuleiroAtualizado2, 2, 'Submarino', "jogador2", modo)
    tabuleiroAtualizado2copy = copy.deepcopy(tabuleiroAtualizado2)
    batalhaNavalDisplay = batalhaNaval1(altura, largura, 0)
    jogo1final, jogo2final = jogadas(0, 0)
    tirostotais1, tiroserrados1, tirosacertados1, ganhou1 = pegarHistDeJogo(jogo1final, 0, 0, 0, False)
    tirostotais2, tiroserrados2, tirosacertados2, ganhou2 = pegarHistDeJogo(jogo2final, 0, 0, 0, False)
    if ganhou1 == True:
        vencedor = "Jogador 1"
    else:
        vencedor = "Jogador 2"
    with open('historico.txt', 'w') as text: #arquivo txt
        text.write(
            f"Seu histórico de partida:\nJogador 1:\nTiros totais = {tirostotais1}\nTiros errados = {tiroserrados1}\n Tiros acertados = {tirosacertados1}\n\nJogador 2:\nTiros totais = {tirostotais2}\nTiros errados = {tiroserrados2}\n Tiros acertados = {tirosacertados2}\n\n Quem venceu foi o {vencedor}")
    reiniciarJogo = input("Você gostaria de reiniciar o jogo?: 'sim' ou 'nao' ")
    reiniciarJogo.lower()
    reiniciarJogo.strip()
    if reiniciarJogo == "sim":
        reiniciar = True
    else:
        reiniciar = False