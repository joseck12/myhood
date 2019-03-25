from django.conf.urls import url
from . import views




urlpatterns=[
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/$',views.create_profile_view,name='profile'),
    url(r'^$', views.display, name='display'),
    url(r'^post/$', views.create_post_view, name='post'),

]
