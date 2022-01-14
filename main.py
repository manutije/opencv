import os
import headDetector
opcion = 'z'

while opcion != 's':
    os.system('clear')
    print('Welcome to tijenet photo editor')
    print('a) ... stract head from image')
    print('s) ... Terminate program')
    opcion = input('Select an option: ')
    print('--------------------------------')
    if opcion == 'a':
        headDetector.strt()
