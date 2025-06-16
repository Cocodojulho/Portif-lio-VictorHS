import random

print("Jogo: Pedra, Papel e Tesoura")
print("Opções: pedra, papel, tesoura")
print("1= Jogador vs Jogador")
print("2= Jogador vs IA")
print("3= Sair")

vitoriasJogador1 = 0
vitoriasJogador2 = 0
vitoriasIA = 0
empates = 0

while True:
    modo = input("Jogador, escolha seu modo de jogo, sendo: 1, 2 ou 3 para sair: ").strip()

    if modo == "3":
        print("Jogo encerrado.")
        print(f"Histórico de partidas:")
        print(f"Vitórias Jogador 1: {vitoriasJogador1}")
        print(f"Vitórias Jogador 2: {vitoriasJogador2}")
        print(f"Vitórias IA: {vitoriasIA}")
        print(f"Empates: {empates}")
        break

    if modo not in ["1", "2"]:
        print("Escolha inválida, tente novamente:")
        continue

    jogador1 = input("Jogador 1, escolha entre: pedra, papel, tesoura. ").strip().lower()

    if jogador1 not in ["pedra", "papel", "tesoura"]:
        print("Resposta inválida, tente novamente:")
        continue

    if modo == "1":
        jogador2 = input("Jogador 2, escolha entre: pedra, papel, tesoura. ").strip().lower()
        if jogador2 not in ["pedra", "papel", "tesoura"]:
            print("Resposta inválida, tente novamente:")
            continue
    else:
        jogador2 = random.choice(["pedra", "papel", "tesoura"])
        print(f"A IA escolheu: {jogador2}")

    if jogador1 == jogador2:
        print("O jogo terminou em empate.")
        empates += 1
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
            (jogador1 == "tesoura" and jogador2 == "papel") or \
            (jogador1 == "papel" and jogador2 == "pedra"):
        print("Jogador 1 venceu.")
        vitoriasJogador1 += 1
    else:
        if modo == "2":
            print("IA venceu.")
            vitoriasIA += 1
        else:
            print("Jogador 2 venceu.")
            vitoriasJogador2 += 1

    print(f"Placar Atual:")
    print(f"Total de vitórias Jogador 1: {vitoriasJogador1}")
    print(f"Total de vitórias Jogador 2: {vitoriasJogador2}")
    print(f"Total de vitórias IA: {vitoriasIA}")
    print(f"Total de empates: {empates}")
    print("    Nova rodada    ")
