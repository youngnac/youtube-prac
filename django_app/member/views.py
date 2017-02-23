from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from member.forms import LoginForm, SignUpForm




@login_required
def my_box_view(request):
    user = request.user
    my_box = user.bookmark_set.all()
    context = {
        'my_box': my_box
    }
    return render(request, 'member/my-box.html', context)


def login_view(request):
    # if reqeust.user:
    #     return re
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect('member:my-box')
            else:
                form.add_error(None, 'Incorrect ID or PW')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'member/login.html', context)


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('video:search_video')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'member/signup.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('member:login')
