##########################
#### Código feito por #### 
##### Ismael Edésio ###### 
########## E #############
#### Matheus Henrique ####
########################## 

import os
os.system('cls')
tabuleiro = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
ganhadores = []
historicoTab = []
win = False
playerX = "X"
playerO = "O"

'''Funções'''
def menu():
    print()
    print('1--> Jogar')
    print()
    print("2--> ENCERRAR")
    print()
    opcao = int(input(" "))

    while opcao != 2:
        if opcao == 1:
            clearscreen()
            os.system('cls')
            Play()
      
        if opcao ==  2:
          print("Fim do jogo!")
          
        print()
        print('1--> JOGAR')
        print()
        print("2--> ENCERRAR")
        print()
        opcao = int(input(" "))

def Play():
    
    while(True):
        gamestatus()
        coordenadas(playerX)

        if(wincheck(playerX) == True):
            break
            
        gamestatus()
        coordenadas(playerO)

        if(wincheck(playerO) == True):
            break

def gamestatus():
    print('')
    for i in range(0,3):
        print()
        print('             ',
              tabuleiro[i][0],' ', tabuleiro[i][1],' ', tabuleiro[i][2])
    print()

def coordenadas(jogador):
    print("TURNO DE "+jogador)
    linha1 = int(input(' LINHA: '))
    coluna1 = int (input(' COLUNA: '))
    print()

    tabuleiro[linha1 - 1][coluna1 - 1] = jogador
    os.system('cls')

def clearscreen():
    for i in range(0,3):
        for j in range(0,3):
            tabuleiro[i][j] = '-'

def wincheck(jogador):
    empate = darempate()
    linha =winline()
    coluna = wincolumn()
    diagonal = windiagonal()

    if(empate == True or linha == True or coluna == True or diagonal == True):
        gamestatus()
        historicoTab.append(tabuleiro)
        return True

def winline():
    for a in range (0,3):
        if tabuleiro[a][0] == 'X' and tabuleiro[a][1] == 'X' and tabuleiro[a][2] == 'X':
            print('X Ganhou!')
            ganhadores.append("X ganhou")
            return True
            
        if tabuleiro[a][0] == 'O' and tabuleiro[a][1] == 'O' and tabuleiro[a][2]== 'O':
            print('O Ganhou!')
            ganhadores.append("O ganhou")
            return True
        
    return False

def wincolumn():
    for k in range (0,3):
        if tabuleiro[0][k] == 'X' and tabuleiro[1][k] == 'X' and tabuleiro[2][k] == 'X' :
            print('X Ganhou!')
            ganhadores.append("X ganhou")
            return True
                  
        if tabuleiro[0][k] == 'O' and tabuleiro[1][k] == 'O' and tabuleiro[2][k] == 'O' :
            print('O Ganhou!')
            ganhadores.append("O ganhou")            
            return True
    return False

def windiagonal():
    if tabuleiro[0][0]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][2] == 'X':
        print ('X Ganhou!')
        ganhadores.append("X ganhou")
        return True
          
    if tabuleiro[0][2]== 'X' and tabuleiro[1][1]== 'X' and tabuleiro[2][0] == 'X':
        print ('X Ganhou!')
        ganhadores.append("X ganhou")
        return True
                  
    if tabuleiro[0][0]== 'O' and tabuleiro[1][1]== 'O' and tabuleiro[2][2] == "O":
        print ('O Ganhou!')
        ganhadores.append("O ganhou")
        return True
          
    if tabuleiro[0][2] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][0] == 'O':
        print('O Ganhou!')
        ganhadores.append("O ganhou")
        return True

    return False

def darempate():
    if (tabuleiro[0][0] != '-' and tabuleiro[0][1] != '-'and tabuleiro[0][2] != '-'):
        if(tabuleiro[1][0] != '-' and tabuleiro[1][1] != '-' and tabuleiro[1][2] != '-'):
            if (tabuleiro[2][0] != '-' and tabuleiro[2][1] != '-' and tabuleiro[2][2] != '-'):
                if (winline() == False and wincolumn() == False and windiagonal() == False):
                    print ("EMPATE!")
                    ganhadores.append("EMPATE")
                    return True
    return False

menu()