from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Member


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    sex = forms.CharField(max_length=2)

    def save(self):
        djangoUser = super().save(commit=False)
        djangoUser.save();

        name = self.cleaned_data.get('name', '')
        age = self.cleaned_data.get('age', '')
        sex = self.cleaned_data.get('sex', '')

        Member.objects.create(user=djangoUser, name=name, age=age, sex=sex)

        return djangoUser
