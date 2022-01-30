import os

# https://www.delftstack.com/howto/python/python-clear-console/
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def pause():
    if os.name in ('nt', 'dos'):
        os.system('pause')
    else:
        input("Press the <Enter> key to continue...")

def init(lines):
    clear()
    print('\n' * lines, end='')

def reset(x,y,lines,columns):
    gotoxy(x,y)
    for i in range(lines):
        print(' ' * columns)

# https://stackoverflow.com/questions/21330632/pythonic-alternative-of-gotoxy-c-code
#class COORD(ctypes.Structure):
#   _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
#
#   def __init__(self,x,y):
#       self.X = x
#       self.Y = y

def gotoxy(x,y):
    #INIT_POS = COORD(y,x)
    if os.name in ('nt', 'dos'):
        print("%c[%d;%df" % (0x1B, y, x), end='', flush=True)
    #    STD_OUTPUT_HANDLE = -11
    #    hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    #    ctypes.windll.kernel32.SetConsoleCursorPosition(hOut, INIT_POS)
    else:
        print("%c[%d;%df" % (0x1B, y, x), end='', flush=True)

# https://www.programcreek.com/python/example/50589/msvcrt.kbhit
# https://stackoverflow.com/questions/5044073/python-cross-platform-listening-for-keypresses
def kbhit():
    try:
        from msvcrt import kbhit
        return kbhit()
    except ImportError:
        import termios, fcntl, sys
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    c = sys.stdin.read(1)
                    print(" c=", c, end='', flush=True)
                    return True
                except IOError:
                    return False
        finally:
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

def hitKey():
    try:
        from msvcrt import getch
        return getch()
    except ImportError:
        return '\n'
