from django.urls import path
from . import views

urlpatterns = [
    path('cats/', views.catList, name="catList"),
    path('machos/', views.machos, name='machos'),
    path('hembras/', views.hembras, name='hembras'),

]