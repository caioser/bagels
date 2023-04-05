import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, um jogo de dedução lógica.
Por Al Sweigart al@inventwithpython.com

Eu estou pensando em um número de {}-dígitos não repetidos.
Tente advinhar quais são. Aqui vai algumas dicas:
Quando eu disser:       Significa que:
    Pico                Um dígito está correto mas na posição errada.
    Fermi               Um dígito está correto e no lugar certo.
    Bagels              Sem dígitos corretos.

Por exemplo, se o número secreto for 248 e seu palpite for 843, as
pistas serão Fermi Pico'''.format(NUM_DIGITS))

    while True: # loop principal do jogo
        # armazenar o número que o jogador precisa advinhar
        secretNum = getSecretNum()
        print('Eu já pensei em um número')
        print('Você tem {} palpites para advinhar'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Continue o loop desde que um palpite válido seja fornceido
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # O Jogador está correto, parar este loop
            if numGuesses > MAX_GUESSES:
                print('Acabaram, os seus palpites')
                print('A resposta era {}'.format(secretNum))

        # Perguntar se o jogador deseja nova partida
        print('Você quer jogar de novo? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    
    print('Obrigado por jogar comigo!')

def getSecretNum():
    """Retorna uma string com dígitos únicos de acordo com a quantidade em NUM_DIGITS"""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Retorna uma string com pico, fermi, begels como dica para o par de
    palpite e número secreto'''
    if guess == secretNum:
        return "Você conseguiu!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Um dígito correto no lugar correto
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Um dígito correto está no lugar errado
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'  # Não há dígitos corretos
    else:
        # Oragniza as dicas em ordem alfabética, assim sua ordem original não entregam o jogo.
        clues.sort()
        # Retornar única string da lista de strings das dicas
        return ' '.join(clues)

# Se o programa for executado (ao invés de importado), inicie o jogo:
if __name__ == '__main__':
    main()