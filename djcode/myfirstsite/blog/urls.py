from django.conf.urls.defaults import *
from django.views.generic import list_detail, date_based
from blog.views import *
from blog.feeds import BlogLatestEntries


feeds = {
    'latest': BlogLatestEntries,
    }

urlpatterns = patterns('',
    url(r'^post/(?P<slug>[a-z-]+)/$', blog_generic_view,
        {'redirect_to': list_detail.object_detail, },
        name="single_post"),
    url(r'^$', blog_generic_view,
        {'redirect_to': list_detail.object_list, },
        name="blog_home"),
    url(r'^category/(\d+)/$', blog_posts_by_category,
        name="blog_posts_by_category"),
    url(r'^search/$', blog_post_search, name="blog_post_search"),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)
    # url(r'^archive/(?P<month>[a-z]+)/(?P<year>\d{4})/$', blog_generic_view,
    #     {'redirect_to': date_based.archive_month, 'date_field': 'published', 'template_name': 'blog/post_list.html', },
    #     name="blog_posts_by_month"),
