from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     url(r'^register',views.register),
    url(r'^user_register$', views.user_register, name='user_register'),
    url(r'^result', views.result),
]