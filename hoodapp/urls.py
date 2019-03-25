from django.conf.urls import url
from . import views




urlpatterns=[
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
