from django.shortcuts import render


def homepage(request):
    return render(request,"index.html")
def login(request):
    return render(request, "login.html")
def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def registrationPage(request):
     return render(request,"register.html")

def package(request):
    return render(request,template_name="package.html")