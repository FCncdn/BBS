from django.conf.urls import url
from .views import mainPage
urlpatterns = [
    url(r'^mainPage/$', mainPage, name='MainPage'),
]