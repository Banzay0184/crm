from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from crm.models import *

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('crm:leads')
    form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('users:sign_in')

def construction(request):
    leads = Lead.objects.all()
    return render(request, 'construction.html', {'leads': leads, })