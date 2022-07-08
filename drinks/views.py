from django.shortcuts import render
from .models import Drink

# Create your views here.
def drinks(request):
    return render(request, 'drinks/all.html', {
        'drinks': Drink.objects.all()
    })

def drink():
    return render(request, 'drinks/show.html', {
        drink: None
    })
