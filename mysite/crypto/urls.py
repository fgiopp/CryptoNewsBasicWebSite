from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), #views is the file and home is the function
    path('prices/', views.prices, name="prices")
]