from django.shortcuts import render

# Create your views here.
def drinks(request):
    return render(request, 'drinks/all.html')
