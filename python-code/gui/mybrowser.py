#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import gtk, webkit
def go_but(widget):
    add = addressbar.get_text()
    if not add.startswith("http://"):
        add = "http://" + add
        addressbar.set_text(add)
    web.open(add)
def new_title(view, frame, title):
    win.set_title(title)

# def on_click_link(view, frame):
#     uri = frame.get_uri()
#     addressbar.set_text(uri)

win = gtk.Window()
win.set_default_size(800, 600)
win.connect("destroy", lambda w: gtk.main_quit())
box1 = gtk.VBox()
win.add(box1)
box2 = gtk.HBox()
box1.pack_start(box2, False)
addressbar = gtk.Entry()
addressbar.connect("activate", go_but)
box2.pack_start(addressbar)
gobutton = gtk.Button("Go")
gobutton.connect("clicked", go_but)
box2.pack_start(gobutton, False)
scroller = gtk.ScrolledWindow()
box1.pack_start(scroller)
web = webkit.WebView()
web.open("http://www.google.com.hk")
web.connect("title_changed", new_title)
# web.connect("load-committed", on_click_link)
scroller.add(web)
win.show_all()
gtk.main()
