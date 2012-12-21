#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import gtk, webkit
# Create a GTK+ window
w = gtk.Window()
w.set_title("Example Editor")
# Terminate the program when the window is closed
w.connect("destroy", gtk.main_quit)

# Instantiate the WebKit renderer
editor = webkit.WebView()
# Load an HTML string into the renderer
editor.load_html_string("<p>This is a <b>test</b>", "file:///")
editor.set_editable(True)
# Add the renderer to the window
# For a full list of standard commands, you can refer to the relevant section of the HTML 5 specification. The QuirksMode website has a really useful compatibility table that you can use to see which of these are supported in various browsers.
def on_click_bold(b):
  editor.execute_script("document.execCommand('bold', false, false)")

b = gtk.Button("_Bold")
b.connect("clicked", on_click_bold)
vb = gtk.VBox()
vb.pack_start(editor, True)
vb.pack_start(b, False)
w.add(vb)
w.show_all()

# Turn over control to the GTK+ main loop
gtk.main()
