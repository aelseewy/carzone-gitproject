from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()

    template = 'pages/home.html'

    data = {
        'teams' : teams,
    }

    return render(request, template, data)

def about(request):
    teams = Team.objects.all()

    template = 'pages/about.html'
    
    data = {
        'teams' : teams,
    }
    return render(request, template, data)

def cars(request):
    template = 'cars/cars.html'
    return render(request, template)

def services(request):
    template = 'pages/services.html'
    return render(request, template)

def contact(request):
    template = 'pages/contact.html'
    return render(request, template)