def computador_escolhe_jogada(n,m):
  retirada_computador = m
  if n < m:
    retirada_computador = n
  else:
    for i in range(m):
      if (n-i)%(m+1) ==0:
        retirada_computador = i
  return retirada_computador

def usuario_escolhe_jogada(n,m):
    retirada_usuario = int(input("\nQuantas peças você vai tirar? "))
    while retirada_usuario > m or retirada_usuario <= 0:
        print("\nOops! Jogada inválida! Tente de novo")
        retirada_usuario = int(input("\nQuantas peças você vai tirar? "))
    return retirada_usuario

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Quantas peças por jogada? "))
    ultima_jogada = 'ninguem'
    retirada_computador = 0
    retirada_usuario = 0

    if n % (m + 1) == 0:
        print("\nVocê Começa!")
        retirada_usuario = usuario_escolhe_jogada(n, m)
        n = n - retirada_usuario
        print("\nO usuario tirou", retirada_usuario, 'peças')
        ultima_jogada = 'jogador'

    else:
        print("\nComputador começa!")
        retirada_computador = computador_escolhe_jogada(n, m)
        n = n - retirada_computador
        print("\nO computador tirou", retirada_computador, 'peças')
        ultima_jogada = 'computador'

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro\n")
    else:
        print("Agora resta apenas", n, "peças no tabuleiro\n")

    while n > 0:
        if ultima_jogada == 'jogador':
            retirada_computador = computador_escolhe_jogada(n, m)
            n = n - retirada_computador
            print("\nO computador tirou", retirada_computador, 'peças')
            ultima_jogada = 'computador'

        elif ultima_jogada == 'computador':
            retirada_usuario = usuario_escolhe_jogada(n, m)
            n = n - retirada_usuario
            print("\nO usuario tirou", retirada_usuario, 'peças')
            ultima_jogada = 'jogador'

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro\n")
        elif n > 1:
            print("Agora resta apenas", n, "peças no tabuleiro\n")
        else:
            print("Fim d jogo! O computador ganhou!")

def campeonato():
  print("\nVocê escolheu campeonato!")
  rodada = 1
  while rodada < 4:
    print("\n**** Rodada",rodada,"****\n")
    partida()
    rodada = rodada + 1
  print("\n**** Final do campeonato! ****")
  print("\nPlacar: Você 0 X 3 Computador")

print("Bem vindo ao jogo do NIM! Escolha: \n")
escolha = int(input("1 - para jogar partida isolada \n2 - para jogar um campeonato 2  "))
if escolha == 1:
  partida()
elif escolha == 2:
  campeonato()
