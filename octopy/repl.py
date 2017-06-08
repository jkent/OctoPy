# -*- coding: utf-8 -*-
# vim: set ts=4 et

import readline
import sys
from textwrap import dedent
from threading import Thread


class REPL(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cmds = {'help': self.on_help, 'exit': self.on_exit}
        self.running = False
        self.confirm_action = None

    def run(self):
        print('Type help for a list of commands')

        self.running = True
        while self.running:
            if self.confirm_action:
                self.prompt = '[y/N] '
                text = input(self.prompt).lower()
                if text.strip().startswith('y'):
                    self.confirm_action()
                self.confirm_action = None
            else:
                self.prompt = 'OctoPy> '
                text = input(self.prompt)
                parts = text.split(maxsplit=1)
                if parts:           
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

    def add_cmd(self, name, func):
        self.cmds[name] = func

    def del_cmd(self, name):
        if name in self.cmds:
            del self.cmds[name]

    def on_help(self, argstr):
        """\
        help [name] - show help
        
        this is an example of a multiline docstring"""
        if not argstr:
            names = list(self.cmds.keys())
            names.sort()
            for name in names:
                parts = self.cmds[name].__doc__.split('\n', 1)
                print(dedent(parts[0]))
        else:
            cmd = self.cmds.get(argstr, None)
            if not cmd:
                print("no such cmd '%s'" % argstr, file=sys.stderr)
            else:
                print(dedent(cmd.__doc__))

    def on_exit(self, argstr):
        """exit - shutdown main"""
        self.running = False
