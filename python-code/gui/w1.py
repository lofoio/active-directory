#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import gtk, sys
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Icon")
        self.connect("destroy", gtk.main_quit)
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        try:
            self.set_icon_from_file("gif/icon_1_01.gif")
        except Exception, e:
            print e.message
            sys.exit(1)
        self.show()
        btn1 = gtk.Button("Button")
        btn1.set_sensitive(False)
        btn2 = gtk.Button("Button")
        btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
        btn4 = gtk.Button("Button")
        btn4.set_size_request(80, 40)

        fixed = gtk.Fixed()

        fixed.put(btn1, 20, 30)
        fixed.put(btn2, 100, 30)
        fixed.put(btn3, 20, 80)
        fixed.put(btn4, 100, 80)

        self.connect("destroy", gtk.main_quit)

        self.add(fixed)
        self.show_all()
PyApp()
gtk.main()
