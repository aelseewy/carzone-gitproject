from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars =Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    template = 'pages/home.html'

    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'all_cars' : all_cars,
    }

    return render(request, template, data)

def about(request):
    teams = Team.objects.all()

    template = 'pages/about.html'
    
    data = {
        'teams' : teams,
    }
    return render(request, template, data)

def services(request):
    template = 'pages/services.html'
    return render(request, template)

def contact(request):
    template = 'pages/contact.html'
    return render(request, template)