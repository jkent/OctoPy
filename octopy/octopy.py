# -*- coding: utf-8 -*-
# vim: set ts=4 et

from .core import Core

def main():    
    print('   ____       __        ____       ')
    print('  / __ \_____/ /_____  / __ \__  __')
    print(' / / / / ___/ __/ __ \/ /_/ / / / /')
    print('/ /_/ / /__/ /_/ /_/ / ____/ /_/ / ')
    print('\____/\___/\__/\____/_/    \__, /  ')
    print('                          /____/   ')
    print('')

    core = Core()
    core.run()

if __name__ == '__main__':
    main()