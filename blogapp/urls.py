from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('politics/', views.politics, name='politics'),
    path('business/', views.business, name='business'),
    path('tech/', views.technology, name='technology'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment')
]
