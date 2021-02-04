from django.conf.urls import url

from . import views #writing all our functions in views

urlpatterns = [
    url('',views.index, name='index') #making index.html as homepage
]
