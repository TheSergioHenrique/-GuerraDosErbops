import console
import jogoLogica

def exibirMenu():
    print("Guerra dos Erbops!-ECOMP2021.1")
    print("Caso você não escolha a dificuldade, o jogo vai começar na dificuldade fácil.")
    print("1 - JOGAR")
    print("2 - CONFIGURACOES E CREDITOS")
    print("3 - SAIR")
    print("                       |    |    |                 ")
    print("                      )_)  )_)  )_)              ")
    print("                     )___))___))___)\            ")
    print("                    )____)____)_____)\ ")
    print("                  _____|____|____|____\__")
    print("         ---------\                   /---------")
    print("           ^^^^^ ^^^^^^^^^^^^^^^^^^^^^")
    print("          ^^^^      ^^^^     ^^^    ^^")
    print("                  ^^^^      ^^^")
    print("Escolha uma opcao: ", end='')

dif = 1

while True:

    opcao = 0
    while (opcao != 1 and opcao != 2 and opcao != 3):
        console.clear()
        exibirMenu()
        try:
            opcao = int(input())
        except:
            opcao = 0

    if (opcao == 1):

        if(dif==1):
            console.clear()
            jogoLogica.historia()
            console.clear()
            jogoLogica.jogarDificuldadeFacil() 
        if(dif==2):
            console.clear()
            jogoLogica.historia()
            console.clear()
            jogoLogica.jogarDificuldadeMediana()
        if(dif==3):
            console.clear()
            jogoLogica.historia()
            console.clear()
            jogoLogica.jogarDificuldadeDificil()  

    elif (opcao == 2):
        console.clear()
        dif = jogoLogica.configurar()

    else:
        exit(0)
