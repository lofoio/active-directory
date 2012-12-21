import gtk
import webkit
view = webkit.WebView()
sw = gtk.ScrolledWindow()
sw.add(view)
win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.add(sw)
win.connect("destroy", gtk.main_quit)
win.show_all()
view.open("file:///home/wangdian/active-directory/my_html/jquery-cheatsheet.html")
gtk.main()
