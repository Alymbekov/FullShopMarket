from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "Hello world",
        "content": "Welcome to the homepage",
    }
    return render(request, "home_page.html", context)


def about_page(request):
    result = get_html("https://yastroymarket.ru/about/")
    print(result)
    soup = BeautifulSoup(result, 'html.parser')
    data = soup.find_all('body')

    context = {
        "title": "This is About Page",
        "content": "Welcome to the About Page",
        "data": data
    }
    print(locals())
    return render(request, "index.html", locals())


def contact_page(request):
    form = ContactForm(request.POST or None)
    context = {
        "title": "This is Contact Page",
        "content": "Welcome to the Contact page",
        "contact": True,
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))

    return render(request, "index.html", context)

import requests
from bs4 import BeautifulSoup
from django.contrib.auth import (
    authenticate, login
)

from django.contrib.auth import get_user_model

from .forms import (
    ContactForm, LoginForm, RegisterForm
)

from django.http import HttpResponse
from django.shortcuts import render, redirect



def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    if form.is_valid():
        username, password = form.cleaned_data.values()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login')
            # A backend authenticated the credentials
        else:
            print("Error")
            # No backend authenticated the credentials
    return render(request, 'auth/login.html', locals())

def register_page(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        User = get_user_model()
        print(form.cleaned_data)
        username = form.cleaned_data.get("username", None)
        email = form.cleaned_data.get("email", None)
        password = form.cleaned_data.get("password", None)
        new_user = User.objects.create_user(
            username, email, password
        )
        if new_user:
            return redirect("/login")

    return render(request, 'auth/register.html', locals())


def get_html(url):
    response = requests.get(url)
    return response.text

def index(request):
    # data = request.session.keys()
    # print(data)
    import random
    random_data = random.choice([x for x in range(1, 50)])
    context = {
        "title": "Hey guys !!!",
        "random": random_data
    } 
    return render(request, "index.html", context)


def index_old(request):
    html_ = """
        <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body> 
        <h1>Hello, world!</h1>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    return HttpResponse(
        html_
        )


