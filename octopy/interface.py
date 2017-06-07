# -*- coding: utf-8 -*-
# vim: set ts=4 et

class SelectableInterface(object):
    def __init__(self, *args, **kwargs):
        self.connected = False

    def fileno(self):
        self.sock.fileno()

    def can_read(self):
        return self.connected

    def can_write(self):
        return False

    def do_read(self):
        pass

    def do_write(self):
        pass
