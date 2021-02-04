from django.conf.urls import url

from . import views #writing all our functions in views

urlpatterns = [
    url('register',views.register, name='register'), #making register.html page
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout')
]
