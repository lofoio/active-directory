#!/usr/bin/python2
import os
import gtk
import webkit
import jswebkit


def show_result(view, frame):
    print frame.get_title()
    print frame.get_uri()
    JSctx = frame.get_global_context()
    ctx = jswebkit.JSContext(JSctx)
    text = ctx.EvaluateScript('document.documentElement.innerHTML')
    print str(text)

webview=webkit.WebView()
sw = gtk.ScrolledWindow()
sw.add(webview)

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.add(sw)
win.show_all()

webview.connect( 'load-finished', show_result )
webview.load_uri('http://www.baidu.com')
frame = webview.get_main_frame()
gtk.main()
