from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, EVSU!")

from django.shortcuts import render
def home(request):
    return render(request, "home.html", {"title": "Home"})

def about(request):
    context = {
        "title": "About",
        "name": "Jerica U. Niemes",        
        "student_id": "2023-25529"   
    }
    return render(request, "about.html", context)