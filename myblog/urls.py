from django.conf.urls import url
from .views import blog_list, blog_detail, test, classification_list
urlpatterns = [
    url(r'^$', blog_list, name='index'),
    url(r'^detail/(?P<id>[0-9]+)', blog_detail, name='detail'),
    url(r'^test/$', test, name='test'),
    url(r'^(?P<classname>.+)' , classification_list, name='classification')

]