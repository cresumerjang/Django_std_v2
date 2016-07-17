from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from accounts.forms import SignupForm
from accounts.models import Member

def signup(request):
    if request.method == 'POST':
        signupField = SignupForm(request.POST)
        if signupField.is_valid():
            signupField.save()
            # next_url = request.GET.get('next', '')
            # return redirect(settings.LOGIN_URL + '?next=' + next_url)
            return redirect(reverse('blog:list') + '?complete')
    else:
        signupField = SignupForm()

    return render(request, 'accounts/signup.html', {
        'viewModel' : signupField,
    })

# 장고 로그인 성공시 기본리다이렉트 url패턴인 profile을 재선언한 메소드
def loginSuccess(request):
    return redirect(reverse('signup'))

@login_required
def myAccount(request):
    # login검증
    # 로그인 필요시 로그인페이지로
    # 로그인 되어있을경우 마이페이지로
    return render(request, 'accounts/my_account.html', {})

def accountList(request):
    viewModel = Member.objects.all()
    return render(request, 'accounts/acount_list.html', {'viewModel' : viewModel,})
# def login(request):
#     viewModel = Member.objects.all()
#     return render(request, 'accounts/list.html', {
#         'viewModel' : viewModel,
#     })
