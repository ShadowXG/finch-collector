from django.shortcuts import render

# Create your views here.

# Home view
def home(request):
  return render(request, 'home.html')

# About view
def about(request):
  return render(request, 'about.html')