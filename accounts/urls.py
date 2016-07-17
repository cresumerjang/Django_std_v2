from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth.views import login, logout
from . import views

# settings.LOGIN_REDIRECT_URL = '/blog/list'

# login redirect 옵션, template옵션 찾기
# logout redirect 옵션, template옵션 찾기
# ?next=/accounts/accountList
#
urlpatterns = [
	# 회원가입
	url(r'^signup/$', views.signup, name='signup'),
	# 로그인
	url(r'^login/$', login, name='login', kwargs={'template_name' : 'accounts/login.html',}),
	# 로그아웃
	url(r'^logout/$', logout, name='logout'),
	# 로그인 성공(리다이렉트처리)
	url(r'^profile/$', views.loginSuccess, name='login_success'),
	# 내 계정
	url(r'^myAccount/$', views.myAccount, name='my_account'),
	# 모든 유저 리스트
	url(r'^accountList/$', views.accountList, name='account_list'),
	# 탈퇴
	url(r'^deleteAccount/$', views.deleteAccount, name='delect_account'),
	# 회원정보 수정
	url(r'^modifyAccount/$', views.modifyAccount, name='modify_account'),
]
