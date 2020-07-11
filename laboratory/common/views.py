from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from common.forms import UserForm

# from .models import Profile


# Create your views here.
def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # 중복체크 추가해야함
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'common/signup.html', context)
