import form as form
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import imagedetails, farmers, articles
from .models import friends


# Create your views here.
def image5(request):
    a = imagedetails.objects.all()
    return render(request, 'html1.html', {'b': a})


def table1(request):
    c = friends.objects.all()
    return render(request, 'html2.html', {'c': c})

# @login_required(login_url='login')
def indextemplate(request):
    index = farmers.objects.all()
    article = articles.objects.all()

    return render(request, 'index.html', {'index': index, 'article': article})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration.Invalid information")
    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}.')

                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    auth.logout(request)

    return redirect("/")
