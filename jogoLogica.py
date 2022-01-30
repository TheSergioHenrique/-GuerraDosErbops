from console import *
from time import *
from random import randrange
from jogoConst import *
import winsound
from jogoMath import solve2
from datetime import *
import os
import threading


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def configurar():
    print("Desenvolvido por Caio Victor, Joel Medeiros, Marcos Prudêncio e Sérgio Henrique, com as orientações de Joabe Jesus.")
    print("CONTROLES: Utilize os botoes W pra subir o barco, S para Descer e ESPAÇO para disparar o projétil.")
    print("Configuracoes do JOGO:")
    print("- Dificuldade:\n  1 - Fácil\n  2 - Mediana\n 3 - Difícil")
    dif = int(input("Escolha a Dificuldade desejada: "))
    while (dif != 1 and dif != 2 and dif !=3):
        dif = int(input("Escolha a Dificuldade desejada: "))
    return dif


def historia():
    gotoxy(LIMITE/5,LIMITE_VERT) 
    print('''                 
                   ()
                   ||q',,'
                   ||d,~
        (,---------------------,)
         ',       q888p       ,'
           \       986       /
            \  8p, d8b ,q8  /
             ) 888a888a888 (
            /  8b` q8p `d8  \              O
           /       689       \             |','
          /       d888b       \      (,---------,)
        ,'_____________________',     \   ,8,   /
        (`__________L|_________`)      ) a888a (    _,_
        [___________|___________]     /___`8`___\   }*{
          }:::|:::::}::|::::::{      (,=========,)  -=-
           '|::::}::|:::::{:|'  .,.    \:::|:::/    ~`~=
--=~(@)~=-- '|}:::::|::{:::|'          ~".,."~`~
              '|:}::|::::|'~`~".,."
          ~`~".,."~`~".,                 "~`~".,."~
                         ".,."~`~
''')
    gotoxy(0,1)
    print("Muito tempo atrás, na idade das trevas, os Erbops dominavam os sete mares.")
    pause()
    print("Porém, um ataque fulminante de piratas deixou os Erpobs em perigo! ")
    pause()
    print("Para se salvarem, os Erbops terão que destruir todos os navios piratas que entrarem em seu caminho.")
    pause()


def jogarDificuldadeFacil():
    os.system('color 2')
    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('=-' * 60, end='', flush=True)
    gotoxy(0,LIMITE_VERT-1)
    print('=-' * 60, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos: 0", end='')
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)

    balas = [ {"x":0, "y":0, "ativa": False, "traj": {"A": 0, "B":0, "C":0} }
            ]

    alvos = [ { "img":"\_-_-_/", "x":0, "y":0, "ativo": False}
            ]
    
    pontuacaoJogador = 0
    intervalo = 5   
    yBarco = LIMITE_VERT-5

    while True:
        gotoxy(LIMITE/120 + 10, 5)
        print("\033[1;36;40m ")
        gotoxy(LIMITE/120 + 3, 7)
        print("               `'-.,_)     `'-.,_)  `   `'-.,_)            `'-.,_)`        `'-.,_)")
        gotoxy(LIMITE/120 + 13, 11)
        print("               `'-.,_)            `'-.,_)        `'-.,_)`'-.,_)        `'-.,_)")
        gotoxy(LIMITE/120 + 4, 15)
        print("               `'-.,_)           '-.,_)`'-.,_)`         `'-.,_)`       `'-.,_)")
        gotoxy(LIMITE/120 + 6, 19)
        print("               `'-.,_)              `'-.,_)     `'-.,_)        `'-.,_)    `'-.,_)")
        gotoxy(LIMITE/120 + 5, 23)
        print("                            `'-.,_)     '-.,_)       `'-.,_)`'-.,_)`'-.,_) ")
    


        for alvo in alvos:  
            if (not alvo["ativo"]):
                alvo["ativo"] = True
                alvo["x"] = 111
                alvo["y"] = randrange(5,28)
                break

        for alvo in alvos:
            gotoxy(alvo["x"], alvo["y"])
            print("         ", end='')
            if alvo["ativo"]:    
                gotoxy(alvo["x"], alvo["y"])
                print(alvo["img"], end='')                
                        

        if (kbhit()):
            c = hitKey()

            if (ord(c) == ord(' ')): 
                for bala in balas:
                    if (not bala["ativa"]):
                        bala["ativa"] = True
                        bala["x"] = 1
                        bala["y"] = yBarco
                        bala["traj"]["A"] = 0.0009
                        bala["traj"]["B"] = -bala["traj"]["A"] * 112
                        bala["traj"]["C"] = yBarco + bala["traj"]["A"] * 112
                        break

            elif (ord(c) == ord('w')) or (ord(c) == ord('W')):
                gotoxy(LIMITE/120, 3)
                print("                                       ")
                yBarco -= 1
                if (yBarco<5):
                    yBarco = 5
                    gotoxy(LIMITE/120, LIMITE_VERT-3)
                    print("O Barco não pode subir mais!")
                gotoxy(LIMITE/120,yBarco-3)
                print('''
                   
                

                
                '''     , end='')
            elif (ord(c) == ord('s')) or (ord(c) == ord('S')):
                gotoxy(LIMITE/120,LIMITE_VERT-3)
                print("                                       ")
                yBarco += 1
                if (yBarco>27):
                    yBarco = 27
                    gotoxy(LIMITE/120,3)
                    print("O Barco não pode descer mais!")    
                gotoxy(LIMITE/120,yBarco-5)
                print('''
                   
                
                
                '''     , end='')
    

        for bala in balas:
            if (bala["ativa"]):
                gotoxy(bala["x"], bala["y"])
                print('  ', end='')
                bala["x"] += 5
                bala["y"] = int(solve2(bala["traj"]["A"], bala["traj"]["B"], bala["traj"]["C"], bala["x"])) 
                if (bala["x"] >= 115):
                    bala["ativa"] = False
                else:
                    gotoxy(bala["x"], bala["y"])
                    print('▒█ ',end='')   

       
        gotoxy(LIMITE/120, yBarco-2)
        print(barco)

        acertou = 0

        for bala in balas:
            for alvo in alvos:
                if (bala["ativa"] and alvo["ativo"]
                        and bala["x"] == alvo["x"]
                        and bala["y"] == alvo["y"]):
                    acertou = True
                    alvo["ativo"] = False
                    bala["ativa"] = False
                    winsound.Beep(500, 200)
                    gotoxy(bala["x"], bala["y"])
                    print('  ', end='')
                    gotoxy(alvo["x"], alvo["y"])
                    print('           ', end='')
                    break
      

        if (acertou):
            pontuacaoJogador += PONTOS_ACERTO
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % pontuacaoJogador, end='')

        fimDoJogo = lambda : pontuacaoJogador >= 10
        if (fimDoJogo()):
            clear()
            gotoxy(0,1)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(0,LIMITE_VERT)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(LIMITE/2-20, LIMITE_VERT-22)
            print("Os piratas foram destuídos!")
            gotoxy(LIMITE/2, LIMITE_VERT - 20)
            print('''        
                        __|__ |___| |
                        |o__| |___| | 
                        |___| |___| |o 
                       _|___| |___| |__o
                    /...\_____|___|____\_/
                    \   o * o * * o o  / 
            ''')
            break

        
        sleep(0.1)
        intervalo -= 1




    pause()

def jogarDificuldadeDificil():

    os.system('color 4')
    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('=-' * 60, end='', flush=True)
    gotoxy(0,LIMITE_VERT-1)
    print('=-' * 60, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos: 0", end='')
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)

    balas = [ {"x":0, "y":0, "ativa": False, "traj": {"A": 0, "B":0, "C":0} }
            ]

    alvos = [ { "img":"\_-_-_/", "x":0, "y":0, "ativo": False,"tempo":0}
            ]
    
    pontuacaoJogador = 0
    intervalo = 5   
    yBarco = LIMITE_VERT-5
    
    def atualizarBarco():
        for alvo in alvos:
            if (alvo["ativo"]):
                gotoxy(alvo["x"], alvo["y"])
                print('           ', end='')
                alvo["ativo"] = False
                winsound.Beep(500, 200)
                gotoxy(bala["x"], bala["y"])
                print('  ', end='')
                gotoxy(alvo["x"], alvo["y"])
                print('           ', end='')

        
    def trocarBarcoLugar():
        atualizarBarco()

    set_interval(trocarBarcoLugar, randrange(5,13))

    while True:
        gotoxy(LIMITE/120, 3)
        print("\033[1;34;40m ")
        gotoxy(LIMITE/120 + 3, 7)
        print("               `'-.,_)     `'-.,_)     `'-.,_)            `'-.,_)`        `'-.,_)")
        gotoxy(LIMITE/120 + 13, 11)
        print("               `'-.,_)            `'-.,_)        `'-.,_)`'-.,_)        `'-.,_)")
        gotoxy(LIMITE/120 + 4, 15)
        print("               `'-.,_)           '-.,_)`'-.,_)`         `'-.,_)       `'-.,_)")
        
        gotoxy(LIMITE/120 + 5, 23)
        print("                            `'-.,_)     '-.,_)       `'-.,_)`'-.,_)`'-.,_) ")

        for alvo in alvos:
            if (not alvo["ativo"]):
                alvo["ativo"] = True
                alvo["x"] = 111
                alvo["y"] = randrange(5,28)
                break


        for alvo in alvos:
            gotoxy(alvo["x"], alvo["y"])
            print("         ", end='')
            if alvo["ativo"]:
                gotoxy(alvo["x"], alvo["y"])
                print(alvo["img"], end='')     

        if (kbhit()):
            c = hitKey()
            if (ord(c) == ord(' ')): 
                for bala in balas:
                    if (not bala["ativa"]):
                        bala["ativa"] = True
                        bala["x"] = 1
                        bala["y"] = yBarco
                        bala["traj"]["A"] = 0.0009
                        bala["traj"]["B"] = -bala["traj"]["A"] * 112
                        bala["traj"]["C"] = yBarco + bala["traj"]["A"] * 112
                        break

            elif (ord(c) == ord('w')) or (ord(c) == ord('W')):
                gotoxy(LIMITE/120, 3)
                print("                                       ")
                yBarco -= 1
                if (yBarco<5):
                    yBarco = 5
                    gotoxy(LIMITE/120, LIMITE_VERT-3)
                    print("O Barco não pode subir mais!")
                gotoxy(LIMITE/120,yBarco-3)
                print('''
                   
                

                
                '''     , end='')
            elif (ord(c) == ord('s')) or (ord(c) == ord('S')):
                gotoxy(LIMITE/120,LIMITE_VERT-3)
                print("                                       ")
                yBarco += 1
                if (yBarco>27):
                    yBarco = 27
                    gotoxy(LIMITE/120,3)
                    print("O Barco não pode descer mais!")    
                gotoxy(LIMITE/120,yBarco-5)
                print('''
                   
                
                
                '''     , end='')
    

        for bala in balas:
            if (bala["ativa"]):
                gotoxy(bala["x"], bala["y"])
                print('  ', end='')
                bala["x"] += 5
                bala["y"] = int(solve2(bala["traj"]["A"], bala["traj"]["B"], bala["traj"]["C"], bala["x"])) 
                if (bala["x"] >= 115):
                    bala["ativa"] = False
                else:
                    gotoxy(bala["x"], bala["y"])
                    print('▒█ ',end='')   

       
        gotoxy(LIMITE/120, yBarco-2)
        print(barco)

        acertou = 0

        for bala in balas:
            for alvo in alvos:
                if (bala["ativa"] and alvo["ativo"]
                        and bala["x"] == alvo["x"]
                        and bala["y"] == alvo["y"]):
                    acertou = True
                    alvo["ativo"] = False
                    bala["ativa"] = False
                    winsound.Beep(500, 200)
                    gotoxy(bala["x"], bala["y"])
                    print('  ', end='')
                    gotoxy(alvo["x"], alvo["y"])
                    print('           ', end='')
                    break
      

        if (acertou):
            pontuacaoJogador += PONTOS_ACERTO
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % pontuacaoJogador, end='')

        fimDoJogo = lambda : pontuacaoJogador >= 10
        if (fimDoJogo()):
            clear()
            gotoxy(0,1)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(0,LIMITE_VERT)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(LIMITE/2-20, LIMITE_VERT-22)
            print("Os erbops finalmente viverão em paz sem a ameaça dos piratas!")
            gotoxy(LIMITE/2, LIMITE_VERT - 20)
            print('''
                     _____ _          _                 _                              _                        _ 
                    |  _  | |        (_)               | |                            (_)                      | |
                    | | | | |__  _ __ _  __ _  __ _  __| | ___    _ __   ___  _ __     _  ___   __ _  __ _ _ __| |
                    | | | | '_ \| '__| |/ _` |/ _` |/ _` |/ _ \  | '_ \ / _ \| '__|   | |/ _ \ / _` |/ _` | '__| |
                    \ \_/ / |_) | |  | | (_| | (_| | (_| | (_) | | |_) | (_) | |      | | (_) | (_| | (_| | |  |_|
                     \___/|_.__/|_|  |_|\__, |\__,_|\__,_|\___/  | .__/ \___/|_|      | |\___/ \__, |\__,_|_|  (_)
                                         __/ |                   | |                 _/ |       __/ |             
                                        |___/                    |_|                |__/       |___/             
            ''')
            break

        sleep(0.1)
        intervalo -= 1

       
    pause()

def jogarDificuldadeMediana():

    os.system('color 3')
    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('=-' * 60, end='', flush=True)
    gotoxy(0,LIMITE_VERT-1)
    print('=-' * 60, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos: 0", end='')
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)

    balas = [ {"x":0, "y":0, "ativa": False, "traj": {"A": 0, "B":0, "C":0} }
            ]

    alvos = [ { "img":"\_-_-_/", "x":0, "y":0, "ativo": False,"tempo":0}
            ]
    
    pontuacaoJogador = 0
    intervalo = 5   
    yBarco = LIMITE_VERT-5
    
    def atualizarBarco():
        for alvo in alvos:
            if (alvo["ativo"]):
                gotoxy(alvo["x"], alvo["y"])
                print('           ', end='')
                alvo["ativo"] = False
                winsound.Beep(500, 200)
                gotoxy(bala["x"], bala["y"])
                print('  ', end='')
                gotoxy(alvo["x"], alvo["y"])
                print('           ', end='')

        
    def trocarBarcoLugar():
        atualizarBarco()

    set_interval(trocarBarcoLugar, randrange(10,20))

    while True:
        gotoxy(LIMITE/120, 3)
        print("\033[1;93;40m ")
        gotoxy(LIMITE/120 + 3, 7)
        print("               `'-.,_)     `'-.,_)     `'-.,_)            `'-.,_)`        `'-.,_)")
        gotoxy(LIMITE/120 + 13, 11)
        print("               `'-.,_)            `'-.,_)        `'-.,_)`'-.,_)        `'-.,_)")
        gotoxy(LIMITE/120 + 4, 15)
        print("               `'-.,_)           '-.,_)`'-.,_)`         `'-.,_)       `'-.,_)")
        
        gotoxy(LIMITE/120 + 5, 23)
        print("                            `'-.,_)     '-.,_)       `'-.,_)`'-.,_)`'-.,_) ")

        for alvo in alvos:
            if (not alvo["ativo"]):
                alvo["ativo"] = True
                alvo["x"] = 111
                alvo["y"] = randrange(10,20)
                break


        for alvo in alvos:
            gotoxy(alvo["x"], alvo["y"])
            print("         ", end='')
            if alvo["ativo"]:
                gotoxy(alvo["x"], alvo["y"])
                print(alvo["img"], end='')     

        if (kbhit()):
            c = hitKey()
            if (ord(c) == ord(' ')): 
                for bala in balas:
                    if (not bala["ativa"]):
                        bala["ativa"] = True
                        bala["x"] = 1
                        bala["y"] = yBarco
                        bala["traj"]["A"] = 0.0009
                        bala["traj"]["B"] = -bala["traj"]["A"] * 112
                        bala["traj"]["C"] = yBarco + bala["traj"]["A"] * 112
                        break

            elif (ord(c) == ord('w')) or (ord(c) == ord('W')):
                gotoxy(LIMITE/120, 3)
                print("                                       ")
                yBarco -= 1
                if (yBarco<5):
                    yBarco = 5
                    gotoxy(LIMITE/120, LIMITE_VERT-3)
                    print("O Barco não pode subir mais!")
                gotoxy(LIMITE/120,yBarco-3)
                print('''
                   
                

                
                '''     , end='')
            elif (ord(c) == ord('s')) or (ord(c) == ord('S')):
                gotoxy(LIMITE/120,LIMITE_VERT-3)
                print("                                       ")
                yBarco += 1
                if (yBarco>27):
                    yBarco = 27
                    gotoxy(LIMITE/120,3)
                    print("O Barco não pode descer mais!")    
                gotoxy(LIMITE/120,yBarco-5)
                print('''
                   
                
                
                '''     , end='')
    

        for bala in balas:
            if (bala["ativa"]):
                gotoxy(bala["x"], bala["y"])
                print('  ', end='')
                bala["x"] += 5
                bala["y"] = int(solve2(bala["traj"]["A"], bala["traj"]["B"], bala["traj"]["C"], bala["x"])) 
                if (bala["x"] >= 115):
                    bala["ativa"] = False
                else:
                    gotoxy(bala["x"], bala["y"])
                    print('▒█ ',end='')   

       
        gotoxy(LIMITE/120, yBarco-2)
        print(barco)

        acertou = 0

        for bala in balas:
            for alvo in alvos:
                if (bala["ativa"] and alvo["ativo"]
                        and bala["x"] == alvo["x"]
                        and bala["y"] == alvo["y"]):
                    acertou = True
                    alvo["ativo"] = False
                    bala["ativa"] = False
                    winsound.Beep(500, 200)
                    gotoxy(bala["x"], bala["y"])
                    print('  ', end='')
                    gotoxy(alvo["x"], alvo["y"])
                    print('           ', end='')
                    break
      

        if (acertou):
            pontuacaoJogador += PONTOS_ACERTO
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % pontuacaoJogador, end='')

        fimDoJogo = lambda : pontuacaoJogador >= 10
        if (fimDoJogo()):
            clear()
            gotoxy(0,1)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(0,LIMITE_VERT)
            print("~" * LIMITE, end='', flush=True)
            gotoxy(LIMITE/2-20, LIMITE_VERT-22)
            print("Os piratas foram destuídos! - Dificuldade Mediana Vencida!!")
            gotoxy(LIMITE/2, LIMITE_VERT - 20)
            print('''        
                        __|__ |___| |
                        |o__| |___| | 
                        |___| |___| |o 
                       _|___| |___| |__o
                    /...\_____|___|____\_/
                    \   o * o * * o o  / 
            ''')
            break

        sleep(0.1)
        intervalo -= 1

       
    pause()