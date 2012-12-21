import os
import gtk
import jswebkit
import lxml.html
import pygtk
import webkit

def load_finished(view, frame):
    # called when the document finishes loading
    if frame != view.get_main_frame():
        return
    ctx = jswebkit.JSContext(frame.get_global_context())
    res = ctx.EvaluateScript('window.location.href')
    print res
    res = ctx.EvaluateScript('document.body.innerHTML')
    tree = lxml.html.fromstring(res)
    print tree.xpath('//input[@type="submit"]')

# initialization
pygtk.require20()
gtk.gdk.threads_init()

# create the webview and hook up callbacks to signals
view = webkit.WebView()
view.set_size_request(1024, 768)
view.connect('load-finished', load_finished)

# configure the webview
props = view.get_settings()
props.set_property('enable-java-applet', False)
props.set_property('enable-plugins', False)
props.set_property('enable-page-cache', False)

# create a window to host the webview
win = gtk.Window()
win.add(view)
win.show_all()

# open google front page
view.open('http://www.google.com')

# spin, processing gtk events
while True:
    try:
        while gtk.events_pending():
            gtk.main_iteration(False)
    except KeyboardInterrupt:
        break
