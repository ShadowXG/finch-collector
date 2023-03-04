from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
]