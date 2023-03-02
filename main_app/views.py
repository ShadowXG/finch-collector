from django.shortcuts import render
# import models here
from .models import Finch

# temporary finches
# finches = [
#     {
#         'species': 'American Goldfinch',
#         'color': 'yellow and black',
#         'description': 'The American goldfinch is a small North American bird in the finch family', 
#         'location': "North America"
#     },
#     {
#         'species': 'Brambling',
#         'color': 'tan and white with black', 
#         'description': 'The brambling is a small passerine bird in the finch family', 
#         'location': "widespread"
#     },
# ]

# Create your views here.

# Home view
def home(request):
  return render(request, 'home.html')

# About view
def about(request):
  return render(request, 'about.html')

# Finches index view
def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })