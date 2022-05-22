"""
Desafio Lets Code
Você já deve ter jogado o Jogo da Forca, certo? O que você acha de desenvolver o seu próprio Jogo
da Forca em Python? Esse será o seu desafio!
Em resumo, ao iniciar o jogo, o jogador receberá uma palavra "codificada", de forma que ele saiba
apenas o número de letras que a compõem. Com base nisso, o jogador deve escolher uma letra
que acredita fazer parte daquela palavra. O jogo acaba quando o jogador erra a letra pela sexta vez
ou quando acerta todas as letras da palavra.
"""

#Solicitar nome do jogador e imprimir boas vidas

jogador = input("Por favor, digite seu nome: ")
print(f"Boas-vindas {jogador}!")

#Perguntar se o usuário já conhece as regras e explica-las.
regras = input("Já conhece as regras do jogo de forca?(s/n) ")

if regras == "s":
    print("Ok, vamos começar o jogo então!")
elif regras == "n":
    print("Você terá que acertar qual é uma palavra sabendo apenas a quantidade de caracteres. Para isso, em cada rodada você escolherá uma letra. Mas cuidado! se a letra escolhida não estiver na palavra, será contado um erro e caso erre seis vezes você perde!")

# Criar lista de palavras e sortear a palavra.
lista_palavras = ["banana","uva","maça","brasil","capital","risco","programa","estudo","familia","livro","batata","beterraba","abacaxi","carne","queijo","televisao","computador","monitor","teclado","mouse","mesa","janela","apartamento","diapasao","harmonia","violao","guitarra","universo","mundo","natal","pascoa","feriado","sabado","domingo","prosopopeia","ambiguidade","chocolate","caramelo","macarrao","cachorro","macaco","elefante","dinossauro","advogado","medico","mendigo","avenida"]

from random import randint
numero_sorteado = randint(0,46)
palavra_sorteada = lista_palavras[numero_sorteado]

# Verificar quantas letras tem na palavra e informar ao usuário
letras = len(palavra_sorteada)
print(f"A palavra tem {letras} letras:")

# Criando e mostrando ao usuario a lista com "_" no lugar das letras
espaco = []
for i in range(letras):
    espaco.append("_ ")
print(espaco)

### Lógica do jogo ###

# atribuindo o parametro de tentativas
tentativas = 6
letras_erradas = []

# Criando loop para quem continue jogando se acertar e que encerre quando completar a palavra ou errar 6 vezes.
while tentativas > 0:
    
    if "_ " in espaco: 

        rodada = input("Digite uma letra: ")

        if rodada in palavra_sorteada:
            print("Você acertou")
                
            n = 0
            for i in palavra_sorteada:
                if i == rodada:
                    espaco[n] = rodada
                n += 1
            print(espaco)    
    
        else:
            tentativas -= 1
            print(f"Você errou, mas ainda tem {tentativas} tentativas")     
            letras_erradas.append(rodada)
        print(f"Você já errou as seguintes letras {letras_erradas}")
        
        if tentativas == 0:
            print("Game over!")

    else:
        print("Parabéns, você ganhou!!")
        break
      


