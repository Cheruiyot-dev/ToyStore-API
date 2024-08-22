from django.urls import path
from toys import views  # Import your views

urlpatterns = [
    path('toys/', views.toy_list, name='toy-list'),  # Maps the 'toys/' URL to the toy_list view
    path('toys/<int:pk>/', views.toy_detail, name='toy-detail'),  # Maps URLs like 'toys/1/' to the toy_detail view
]
