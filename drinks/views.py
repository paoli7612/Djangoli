from django.shortcuts import render

from .models import Drink

# Create your views here.
def drinks(request):
    return render(request, 'drinks.html', {'drinks': Drink.objects.all()})

def contacts(request):
    return render(request, 'contact.html')