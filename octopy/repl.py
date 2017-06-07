# -*- coding: utf-8 -*-
# vim: set ts=4 et

import readline
import sys
from threading import Thread

class REPL(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cmd_prompt = 'OctoPy> '
        self.yn_prompt = '[y/N] '
        self.hooks = {'help': self.on_help, 'exit': self.on_exit}
        self.running = False
        self.confirm_action = None

    def run(self):
        print('Type help for a list of commands')

        self.running = True
        while self.running:
            if self.confirm_action:
                text = input(self.yn_prompt).lower()
                if text.strip().startswith('y'):
                    self.confirm_action()
                self.confirm_action = None
            else:
                text = input(self.prompt)
                parts = text.split(maxsplit=1)
                argstr = '' if len(parts) < 2 else parts[1]            
                cmd = self.cmds.get(parts[0], {})
                if not cmd:
                    print("'%s' is not a valid command" % parts[0], file=sys.stderr)
                    continue
                cmd(argstr)
    def print(self, text):
        print('\x1B[G\x1B[2K', end='', flush=True)
        print(text)
        print(self.prompt + readline.get_line_buffer(), end='', flush=True)

    def hook(self, name, func):
        self.hooks[name] = func

    def on_help(self, argstr):
        """help [name] - show help"""
        if not argstr:
            names = list(self.hooks.keys())
            names.sort()
            for name in names:
                parts = self.hooks[name].__doc__.split('\n', 1)
                print(parts[0])
        else:
            hook = self.hooks.get(argstr, None)
            if not hook:
                print("no such hook '%s'" % argstr, file=sys.stderr)
            else:
                print(hook.__doc__)

    def on_exit(self, argstr):
        """exit - shutdown OctoPy"""
        self.running = False
