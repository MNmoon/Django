
from django.conf.urls import url,include
from django.contrib import admin
from .models import Register
from . import views


app_name = 'login'
urlpatterns = [
    # ex: /login/
    url(r'^$', views.regist, name='login'),
    url(r'^$', views.login, name='login'),
]
