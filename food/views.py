from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DateDetailView,DetailView
from django.views.generic.edit import DeleteView
from .models import FoodItem


def index(request):
    context = {
        'food_items' : FoodItem.objects.all()
    }
    return render(request,'food/index.html',context)


class FoodListView(ListView):
    model = FoodItem
    template_name = 'food/index.html'
    context_object_name = 'food_items'


class FoodDetailView(DetailView):
    model = FoodItem
    template_name = 'food/food_detail.html'


class FoodCreateView(CreateView):
    model = FoodItem
    fields = ['name','desc','price','image']
    template_name = 'food/food_create.html'


class FoodUpdateView(UpdateView):
    model = FoodItem
    fields = ['name','desc','price','image']


class FoodDeleteView(DeleteView):
    model = FoodItem
    success_url = '/'