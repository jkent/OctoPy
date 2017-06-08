# -*- coding: utf-8 -*-
# vim: set ts=4 et

from .repl import REPL
import time


class Core(object):
    def __init__(self):
        self.repl = REPL();
        self.repl.start()
    
    def run(self):
        time.sleep(2)
        while self.repl.running:
            self.repl.print('test')
            time.sleep(2)
