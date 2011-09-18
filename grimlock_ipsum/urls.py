from django.conf.urls.defaults import patterns, include, url

from views import HomeView, GrimlockIpsumView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^words/$', GrimlockIpsumView.as_view(), name="grimlock_ipsum"),
)
