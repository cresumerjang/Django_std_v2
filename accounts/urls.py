from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth.views import login, logout
from . import views

# settings.LOGIN_REDIRECT_URL = '/blog/list'

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'), # 회원가입
	url(r'^login/$', login, name='login', kwargs={ # 로그인
		'template_name' : 'accounts/login.html',
	}),
	url(r'^logout/$', logout, name='logout'), # 로그아웃
	url(r'^profile/$', views.loginSuccess, name='login_success'), # 로그인 성공(리다이렉트처리)
	url(r'^myAccount/$', views.myAccount, name='my_account'), # 내 계정
	url(r'^accountList/$', views.accountList, name='account_list'), # 내 계정
]
