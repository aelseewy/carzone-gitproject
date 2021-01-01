from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars =Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    template = 'pages/home.html'

    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'all_cars' : all_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,

#       'search_fields': search_fields,
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