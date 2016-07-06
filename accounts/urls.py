from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^list/$', views.list, name='list'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
]
