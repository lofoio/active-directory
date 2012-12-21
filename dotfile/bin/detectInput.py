#!/usr/bin/python2.6
# -*- coding: iso-8859-15 -*-
import time
import os
import threading
from functools import partial
import sys

class DetectInput(object):
    def __init__(self):
        self.inputPath = '/dev/input/by-path/'
        self.devices = os.listdir(self.inputPath)

        kbd = []
        mouse = []
        for dev in self.devices:
            if dev.find('event') >= 0:
                if dev.find('kbd') >= 0:
                    kbd.append(dev)
                if dev.find('mouse') >= 0:
                    mouse.append(dev)
        self.mouses = mouse
        self.keyboards = kbd

        self.hitsMouses = {}
        self.hitsKeyboards = {}
        self.live = True

    def runKeyboard(self):
        """Start threads om de toetsenborden in de gaten te houden"""
        for dev in self.keyboards:
            threading.Thread(target=partial(self.cmdKeyboard, dev)).start()

    def runMouse(self):
        """Start threads om de muizen in de gaten te houden"""
        for dev in self.mouses:
            threading.Thread(target=partial(self.cmdMouse, dev)).start()

    def cmdMouse(self, dev):
        """Functie die uit wordt gevoerd door runMouse()"""
        self.hitsMouses[dev] = False
        f = open(self.inputPath + dev, 'rb')
        while self.live:
            f.read(500) # 144 kan eigenlijk alles zijn, behalve absurbt hoge waarden..
            self.hitsMouses[dev] = True
            time.sleep(0.1)

    def cmdKeyboard(self, dev):
        """Functie die uit wordt gevoerd door runKeyboard()"""
        # Slaap één-tiende van een seconde om te voorkomen dat de toetsaanslag <enter>
        # wordt gepakt als het wordt uitgevoerd in een terminal
        time.sleep(0.1)

        self.hitsKeyboards[dev] = False
        f = open(self.inputPath + dev, 'rb')
        f.flush()
        while self.live:
            # Lees de toetsaanslag --> Pak de 42ste byte
            self.hitsKeyboards[dev] = f.read(144)[42]
            time.sleep(0.1)

    def die(self):
        """Sluit af."""
        self.live = False

    def map(self, code):
        # Zie documentatie in the kernel broncode: include/linux/input.h
        # <---->
        dic = { 10 : 9,
                11 : 0,
                16 : 'Q',
                17 : 'W',
                18 : 'E',
                19 : 'R',
                20 : 'T',
                2 : 1,
                21 : 'Y',
                22 : 'U',
                23 : 'I',
                24 : 'O',
                25 : 'P',
                30 : 'A',
                31 : 'S',
                3 : 2,
                32 : 'D',
                33 : 'F',
                34 : 'G',
                35 : 'H',
                36 : 'J',
                37 : 'K',
                38 : 'L',
                4 : 3,
                44 : 'Z',
                45 : 'X',
                46 : 'C',
                47 : 'V',
                48 : 'B',
                49 : 'N',
                50 : 'M',
                5 : 4,
                6 : 5,
                7 : 6,
                8 : 7,
                9 : 8,
            }

        try:
            return(dic[code])
        except KeyError:
            return(False)

    def detectKeyboard(self):
        """Detecteer welk toets op welk toetsenbord wordt aangeslagen.

        De output van deze functie is dan ook (<device>, <toets>)."""
        self.runKeyboard()
        time.sleep(0.2)
        searching = True
        while searching:
            for dev in self.keyboards:
                if self.hitsKeyboards[dev] != False:
                    return(dev, self.map(self.hitsKeyboards[dev]))
                time.sleep(0.01)

    def detectMouse(self):
        """Detecteer of een muis bewogen is en geef het device terug"""
        self.runMouse()
        time.sleep(0.1)
        searching = True
        while searching:
            for dev in self.mouses:
                if self.hitsMouses[dev]:
                    return(dev)
            #time.sleep(0.0001)

    def reset(self):
        """Reset alle waarden in de lists waar bijgehouden wordt of
        een muis/toetsenbord actief is geweest."""
        for dev in self.mouses:
            self.hitsMouses[dev] = False

        for dev in self.keyboards:
            self.hitsKeyboards[dev] = False

if __name__ == '__main__':
    x = DetectInput()

    for seat in xrange(len(x.keyboards)):
        print("Detecting keyboard of seat %i." % seat)
        print(x.detectKeyboard()[0])
        print("Detecting mouse of seat %i." % seat)
        print(x.detectMouse())

    #sys.exit(0)
    print('\nClose this terminal :-)')
