from django.shortcuts import render

# temporary finches
finches = [
    {
        'species': 'American Goldfinch', 
        'description': 'The American goldfinch is a small North American bird in the finch family', 
        'location': "North America"
    },
    {
        'species': 'Brambling', 
        'description': 'The brambling is a small passerine bird in the finch family', 
        'location': "widespread"
    },
]

# Create your views here.

# Home view
def home(request):
  return render(request, 'home.html')

# About view
def about(request):
  return render(request, 'about.html')

# Finches index view
def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', { 'finches': finches })