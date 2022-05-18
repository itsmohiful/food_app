from django.urls import path
from . import views


urlpatterns = [
    path('',views.FoodListView.as_view(), name='index'),
    path('detail/<int:pk>/',views.FoodDetailView.as_view(), name='food-detail'),
    path('create/new',views.FoodCreateView.as_view(), name='food-create'),
    path('food/<int:pk>/update',views.FoodUpdateView.as_view(), name='food-update'),
    path('food/<int:pk>/delete',views.FoodDeleteView.as_view(), name='food-delete'),
]