
import requests
from bs4 import BeautifulSoup

from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import render



def get_html(url):
    response = requests.get(url)
    return response.text

def index(request):
    import random
    random_data = random.choice([x for x in range(1, 50)])
    context = {
        "title": "Hey guys !!!",
        "random": random_data
    } 
    return render(request, "index.html", context)


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
    form =  ContactForm(request.POST or None)
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


