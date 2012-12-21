#!/usr/bin/env python2

import gtk
import webkit

class WebView(webkit.WebView):
    def get_html(self):
        self.execute_script('oldtitle=document.title;document.title=document.documentElement.innerHTML;')
        html = self.get_main_frame().get_title()
        self.execute_script('document.title=oldtitle;')
        return html

window = gtk.Window()

view = WebView()
view.open('http://www.google.com')
window.add(view)
window.show_all()
window.connect('delete-event', lambda window, event: gtk.main_quit())
print view.get_html()
gtk.main()
