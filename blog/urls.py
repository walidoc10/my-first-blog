from django.conf.urls import url, include
from . import views

post_urlpatterns = [
    url(r'^$', views.PostView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.DetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreate.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdate.as_view(), name='post_update'),
]

urlpatterns = [
    url(r'', include(post_urlpatterns)),
]
