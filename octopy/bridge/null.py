# -*- coding: utf-8 -*-
# vim: set ts=4 et

from . import BaseBridge


class NullBridge(BaseBridge):
    def __init__(self, mosi, miso, name):
        BaseBridge.__init__(self, name)

    def run(self):
        pass
