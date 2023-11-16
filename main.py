import time
from random import randrange


print('Bem-vindo ao jogo da velha!')

# Criando o tabuleiro vazio
tabuleiro = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {tabuleiro[i][0]}   |   {tabuleiro[i][1]}   |   {tabuleiro[i][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Função para armazenar no tabuleiro a jogada do usuário
def jogada_usuario(tabuleiro, escolha_user):
    encontrou = False
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == escolha_user:
                tabuleiro[i][j] = 'O'
                encontrou = True

    if encontrou:
        print(f'Número {escolha_user} encontrado e modificado para "O"')
    else:
        print(f'Número {escolha_user} ocupado. Escolha outro.')

    return encontrou

# Função para determinar a jogada do PC
def jogada_computador(tabuleiro):
    loop = True
    encontrou_pc = False

    while loop:
        jogada_pc = str(randrange(1, 10))

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == jogada_pc:
                    tabuleiro[i][j] = 'X'
                    encontrou_pc = True
                    loop = False

        if encontrou_pc:
            print(f'Número {jogada_pc} escolhido pelo PC.')

    return tabuleiro

# Função para determinar o vencedor do jogo
def vencedor_jogo(tabuleiro):
    # Horizontal - PC
    vitoria = ''
    for linha in tabuleiro:
        if all(elemento == 'X' for elemento in linha):
            print('O PC venceu - Linhas horizontais.')
            vitoria = 'pc'
            break

    # Vertical - PC
    for coluna in range(3):
        if all(tabuleiro[i][coluna] == 'X' for i in range(3)):
            vitoria = 'pc'
            print('O PC venceu - Linhas verticais')

            break

    # Diagonal - PC
    if all(tabuleiro[i][i] == 'X' for i in range(3)):
        vitoria = 'pc'
        print('O PC venceu - Diagonal principal')

    # Diagonal invertida - PC
    if all(tabuleiro[i][2 - i] == 'X' for i in range(3)):
        vitoria = 'pc'
        print('O PC venceu - Diagonal secundária')

    # Horizontal - USER
    for linha in tabuleiro:
        if all(elemento == 'O' for elemento in linha):
            vitoria = 'user'
            print('Você venceu - Linhas horizontais.')
            break

    # Vertical - USER
    for coluna in range(3):
        if all(tabuleiro[i][coluna] == 'O' for i in range(3)):
            vitoria = 'user'
            print('Você venceu - Linhas verticais')
            break

    return vitoria

# Exibe o tabuleiro e explica que o usuário jogará com o O
imprimir_tabuleiro(tabuleiro)
print('O computador é jogará com o X, você com o O.')
time.sleep(1)

# Primeira jogada padrão do computador
print('\nÉ a vez do computador.')
tabuleiro[1][1] = 'X'
imprimir_tabuleiro(tabuleiro)

# Faz um loop de jogadas até que haja um vencedor ou velha
loop_jogo = 0
while loop_jogo < 4:
    vencedor = ''
    print('\nÉ a sua vez.')

    # Loop para que o jogador jogue novamente caso escolha uma opção ocupada
    repetir_jogada = True
    while repetir_jogada:
        # Invoca a função para jogada do usuário
        escolha_user = str(input('Escolha um número:\n'))
        encontrou = jogada_usuario(tabuleiro, escolha_user)
        # Se não for uma tabela ocupada, sai do loop
        if encontrou:
            imprimir_tabuleiro(tabuleiro)
            repetir_jogada = False

    # Determina se o jogador venceu após a jogada
    if loop_jogo > 1:
        vencedor = vencedor_jogo(tabuleiro)
        if 'user' in vencedor:
            loop_jogo = 5
            break

    # Invoca a função para a jogada do PC
    print('\nÉ a vez do computador.')
    tabulerio = jogada_computador(tabuleiro)
    imprimir_tabuleiro(tabuleiro)

    # Determina se o PC ganhou após a jogada
    if loop_jogo > 1:
        vencedor = vencedor_jogo(tabuleiro)
        if 'pc' in vencedor:
            loop_jogo = 5
            break

    loop_jogo += 1

# Se após o loop não houver vencedor, informa que deu velha
if loop_jogo == 4 and len(vencedor) == 0:
    print('Velha!')
