urlpatterns = patterns('',

       (r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'E:/media'}),

}
<p><img src="/site_media/gmshi.jpg" mce_src="site_media/gmshi.jpg" width="1240" height="949"></p>
然后将gmshi.jpg放入E:/media

Django框架OSCSSXHTML
django 框架， 模板在templates中 ，样式和图片在site_media，
如
templates/index.html
文件内容:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="/site_media/admin/css/manager.css" rel="stylesheet" type="text/css" media="screen" />

<link href="/site_media/admin/css/manager.css" rel="stylesheet" type="text/css" media="screen" />
没有没什么方法可以在templates中的文件只用写 <link href="css/manager.css" rel="stylesheet" type="text/css" media="screen" />
这样美工做完页面后只用拿过来加入数据就可以了，而不用在改样式图片的路径。



在url.py中

import os
site_media = os.path.join(
    os.path.dirname(__file__),'site_media/admin/css/'
)
然后
urlpatterns = patterns('',
     (r'^css/(?P<path>.*)$','django.views.static.serve',
        { 'document_root': site_media }),
就可以了。
