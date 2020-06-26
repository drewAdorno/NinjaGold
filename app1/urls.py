from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/<str:place>', views.process_money),
    path('newgame', views.new_game)
]