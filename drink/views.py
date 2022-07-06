from django.shortcuts import render
from .models import Drink

# Create your views here.

def drink(request):
    drinks = Drink.objects.all()
    return render(request, 'drink/drink.html', {
        'drinks': drinks
    })