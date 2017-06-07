# -*- coding: utf-8 -*-
# vim: set ts=4 et

from multiprocessing import Process, Queue, current_process
from ..interface import SelectableInterface


class BaseBridge(Process, SelectableInterface):
    def __init__(self, name):
        Process.__init__(self, name='Bridge:%s')
        SelectableInterface.__init__(self)
        self.mosi = Queue(5)
        self.miso = Queue(5)
        self.connected = True
 
    def fileno(self):
        if current_process().name == 'MainProcess':
            return self.miso._reader.fileno()
        else:
            return self.mosi._reader.fileno()

    def do_read(self):
        if current_process().name == 'MainProcess':
            while not self.miso.empty():
                d = self.miso.get()
                self.core.handle_input(d['from'], d['data'])
        else:
            while not self.mosi.empty():
                d = self.mosi.get()
                self.process_input(d['data'])
        
    def send(self, data):
        if current_process().name == 'MainProcess':
            d = {'data': data}
            self.mosi.put(d)
        else:
            d = {'from': self.name, 'data': data}
            self.miso.put(d)
