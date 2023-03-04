from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# import models here
from .models import Finch
from .forms import SitingForm

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

# Detail route for finches
def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    siting_form = SitingForm()

    return render(request, 'finches/detail.html', { 'finch': finch, 'siting_form': siting_form })

def add_siting(request, finch_id):
    form = SitingForm(request.POST)

    if form.is_valid():
        new_siting = form.save(commit=False)
        new_siting.finch_id = finch_id
        new_siting.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'location']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'