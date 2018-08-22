from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SigninForm, SignupForm

# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username = email, password = password)
            user1 = User.objects.filter(email = email)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:profile'))
            if user1.count() == 1:
                user1 = authenticate(username = user1[0].username, password = password)
                if user1 is not None:
                    login(request, user1)
                    return HttpResponseRedirect(reverse('accounts:profile'))
                else:
                    return render(request, 'accounts/signin.html', {'form': form, 'error': 'email or password incorrect'})
            else:
                return render(request, 'accounts/signin.html', {'form': form, 'error': 'email or password incorrect'})
        else:
            return render(request, 'accounts/signin.html', {'form': form})
    else:
        form = SigninForm()
        return render(request, 'accounts/signin.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = None
            username = form.cleaned_data['username']
            em = form.cleaned_data['email']
            psw = form.cleaned_data['password']
            psw_repeat = form.cleaned_data['password_repeat']
            if not User.objects.filter(email=em):
                user = User.objects.create_user( email = em, username = username, password = psw)
                user.save()
            if user is None:
                return render(request, 'accounts/signup.html', {'form':form, 'error': 'field is not correct'})
            else:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url = 'accounts:signin')
def profile(request):
    user = request.user
    saved_recommendations = request.user.saver_set.all()
    my_recommendations = request.user.recommendation_set.all()
    return render(request, 'accounts/profile.html', {
        'user': user,
        'saved_recommendations': saved_recommendations,
        'my_recommendations': my_recommendations
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('static_pages:index'))