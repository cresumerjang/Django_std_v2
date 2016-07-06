from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from accounts.forms import SignupForm
from accounts.models import Member

def signup(request):
    if request.method == 'POST':
        signupField = SignupForm(request.POST)
        if signupField.is_valid():
            signupField.save()
            return redirect(reverse('blog:list') + '?complete')
    else:
        signupField = SignupForm()

    return render(request, 'accounts/signup.html', {
        'viewModel' : signupField,
    })

def list(request):
    viewModel = Member.objects.all()
    return render(request, 'accounts/list.html', {
        'viewModel' : viewModel,
    })
