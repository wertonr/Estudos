"""
Desafio Lets Code
Você já deve ter jogado o Jogo da Forca, certo? O que você acha de desenvolver o seu próprio Jogo
da Forca em Python? Esse será o seu desafio!
Em resumo, ao iniciar o jogo, o jogador receberá uma palavra "codificada", de forma que ele saiba
apenas o número de letras que a compõem. Com base nisso, o jogador deve escolher uma letra
que acredita fazer parte daquela palavra. O jogo acaba quando o jogador erra a letra pela sexta vez
ou quando acerta todas as letras da palavra.
"""
import random
import os

#Solicitar nome do jogador e imprimir boas vidas

jogador = input("Por favor, digite seu nome: ")
print(f"\nBoas-vindas {jogador}!")

#Perguntar se o usuário já conhece as regras e explica-las.
regras = input("\nJá conhece as regras do jogo de forca?(s/n) ").upper()

if regras == "S":
    print("Ok, vamos começar o jogo então!")
elif regras == "N":
    print("Você terá que acertar qual é uma palavra sabendo apenas a quantidade de caracteres. Para isso, em cada rodada você escolherá uma letra. Mas cuidado! se a letra escolhida não estiver na palavra, será contado um erro e caso erre seis vezes você perde!")

input("\nPressione Enter para começar o jogo")
os.system('cls')

# Criar lista de palavras e sortear a palavra.
lista_palavras = ["banana","uva","maça","brasil","capital","risco","programa","estudo","familia","livro","batata","beterraba","abacaxi","carne","queijo","televisao","computador","monitor","teclado","mouse","mesa","janela","apartamento","diapasao","harmonia","violao","guitarra","universo","mundo","natal","pascoa","feriado","sabado","domingo","prosopopeia","ambiguidade","chocolate","caramelo","macarrao","cachorro","macaco","elefante","dinossauro","advogado","medico","mendigo","avenida"]

palavra_sorteada = random.choice(lista_palavras).upper()

# Verificar quantas letras tem na palavra e informar ao usuário
letras = len(palavra_sorteada)
print(f"A palavra tem {letras} letras:")

# Criando e mostrando ao usuario a lista com "_" no lugar das letras
espaco = ['_']*letras
print(' '.join(espaco))

### Lógica do jogo ###


# atribuindo o parametro de tentativas
tentativas = 6
letras_erradas = []

# Criando loop para quem continue jogando se acertar e que encerre quando completar a palavra ou errar 6 vezes.
while tentativas > 0:
    
    if "_" in espaco: 

        rodada = input("\nDigite uma letra: ").upper()

        if rodada in palavra_sorteada:
            print("\nVocê acertou")
                
            n = 0
            for i in palavra_sorteada:
                if i == rodada:
                    espaco[n] = rodada
                n += 1
            print(' '.join(espaco))    
    
        else:
            tentativas -= 1
            print(f"\nVocê errou, mas ainda tem {tentativas} tentativas")     
            letras_erradas.append(rodada)
        print(f"\nVocê já errou as seguintes letras: {', '.join(letras_erradas)}")
        
        if tentativas == 0:
            print("\nGame over!")
            print("\nA palavra era: ", palavra_sorteada)
    else:
        os.system('cls')
        print("\nParabéns, você ganhou!!")
        print("\nA palavra era: ", palavra_sorteada)
        print('\n')
        break
      


