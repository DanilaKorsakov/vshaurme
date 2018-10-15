from django.conf.urls import include, url
from . import views as signup
from django.contrib.auth import views


urlpatterns = [
	url(r'^accounts/signup/$', signup.user_new,  name='signup'),
	url(r'^accounts/login/$', views.login, name='login'),
	url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
