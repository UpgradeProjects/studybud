from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.reg, name='reg'),
    path('logout', views.logout, name='logout')
]
