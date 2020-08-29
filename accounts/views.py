from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.

def login(request):
    if request.method == 'POST':
        forms = AuthenticationForm(request, request.POST)
        if forms.is_valid():
            user = forms.get_user()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        forms = AuthenticationForm()
    context = {
        'forms': forms
    }
    return render(request, 'accounts/login.html', context)