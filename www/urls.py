from django.conf.urls import patterns, include, url

urlpatterns = patterns('www.views',
    url(r'^$', 'index', name='www_index'),
    #url(r'token$', 'token', name='www_token'),
    url(r'^plan/(?P<name>\w+)_(?P<gender>\w+).html$', 'plan', name='www_plan'),
    url(r'(?P<name>\w+)$', 'ename', name='www_ename'),
)
