from django.shortcuts import render
from .models import Pet

# Create your views here.
def pets_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets_list.html', {'pets': pets})