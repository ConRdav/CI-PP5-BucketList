from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='wishlist'),
    path('add/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]