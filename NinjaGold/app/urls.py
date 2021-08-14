from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/', views.process),
    path('reset/', views.reset),
]
