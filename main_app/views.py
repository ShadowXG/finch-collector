from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# import models here
from .models import Finch, Food
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

    id_list = finch.foods.all().values_list('id')

    foods_finch_doesnt_have = Food.objects.exclude(id__in=id_list)

    siting_form = SitingForm()

    return render(request, 'finches/detail.html', { 'finch': finch, 'siting_form': siting_form, 'foods': foods_finch_doesnt_have })

def add_siting(request, finch_id):
    form = SitingForm(request.POST)

    if form.is_valid():
        new_siting = form.save(commit=False)
        new_siting.finch_id = finch_id
        new_siting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.add(food_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_food(request, finch_id, food_id):
    Finch.objects.get(id=finch_id).foods.remove(food_id)
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

# FoodList
class FoodList(ListView):
    model = Food
    template_name = 'foods/index.html'

# FoodDetail
class FoodDetail(DetailView):
    model = Food
    template_name = 'foods/detail.html'

# FoodCreate
class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'attracted_birds']

    # define what the inherited method is_valid does(we'll update this later)
    def form_valid(self, form):
        # we'll use this later, but implement right now
        # we'll need this when we add auth
        # super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)

# FoodUpdate
class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'attracted_birds']

# FoodDelete
class FoodDelete(DeleteView):
    model = Food
    template_name = '/foods/'