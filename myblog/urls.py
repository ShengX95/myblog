from django.conf.urls import url
from .views import blog_list, blog_detail, test
urlpatterns = [
    url(r'^$', blog_list, name='index'),
    url(r'^(?P<id>[0-9]+)', blog_detail, name='detail'),
    url(r'^test/$', test, name='test'),

]