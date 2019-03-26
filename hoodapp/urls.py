from django.conf.urls import url
from . import views




urlpatterns=[
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/$',views.create_profile_view,name='profile'),
    url(r'^$', views.display, name='display'),
    url(r'^post/$', views.create_post_view, name='post'),
    url(r'^bizz/$', views.create_buisiness_view, name='bizz'),
    url(r'^business/$', views.business, name='business'),
    url(r'^add/$', views.create_community, name='community'),
]
