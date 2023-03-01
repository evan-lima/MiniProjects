from os import system, name 

#entrada e validação
def input_word(in_word = ''):
    word = ''
    in_word = input('Digite a palavra secreta: ')
    if (in_word.isdigit == True) or (len(in_word) < 3 ):
        print('Entrada inválida! \n* Não utilize números\n* Apenas palavras maiores que 3 caracteres')
        return input_word()
    table = in_word.maketrans('', '', '.,-_!')
    word = in_word.translate(table)
    word = word.lower()
    return word

#Limpa tela
def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 


#Boas vindas, e saída
def welcome(round):
    if round == 0:
        print('Bem Vindo(a)(e)!')
        print('Este é um jogo da forca, você terá 7 tentativas, vamos la!')
        return
    print('Mais uma rodada? [n]\n -Para continuar aperte qualquer tecla-')
    decision = input('')
    if decision != 'n':
        print('Boa Sorte!')
        return
    print('Até Logo!')
    return False

#Tentativas
def attempt(letra = ''):
    letra = input('Tente uma letra: ')
    if len(letra) > 1:
        print('Apenas uma letra por vez espertinho!, tente novamente')
        attempt()
    letra = letra.lower()
    return letra

round = 0
hidden_word = []
game_word = []
letter = ''
round_letter = 0
game_round = 0
all_letters = ''
while True:

    game = welcome(game_round)
    #caso retorne falso, fecha o programa, com a despedida da função
    if game == False:
        break
    
    
    secret_word = input_word()
    hidden_word = list(secret_word)
    game_word = len(hidden_word) * '*' #oculta a palavra
    game_word = list(game_word)
    print(f'Sua palavra secreta é: {secret_word}')

    player2 = input('Aperte qualquer tecla e passe para o Player 2!') #pausa para trocar de jogador

    clear()
    
    while True:
        print('Vamos lá')
        
        print(f'Suas tentativas : {all_letters} você possui {(7 -round)}')
        

        letter  = attempt()
        indice = 0
        executado = False # caso if não tenha sido executado, diminui uma chance
        for letra in hidden_word:
            if letra == letter:
                game_word[indice] = letra
                print(game_word)
                executado = True
                
           
            indice += 1 

        if executado == False:
            round += 1

        all_letters = all_letters + ' - ' + letter #letras tentadas
        

        if round == 7:
            print(f'Suas chances acabaram, a palavra era {hidden_word}')
            break


        if game_word.count('*') == 0:
            print(f'Parabéns, você venceu! com {(round - 7)} tentativas restantes!')
            break
    
    game_round =+ 1

    

