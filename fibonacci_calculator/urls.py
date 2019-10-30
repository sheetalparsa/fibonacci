from django.urls import path

from . import views

urlpatterns = [
    path('calculate', views.calc_fib, name='calculate_fib'),
    path('', views.index, name='index'),
]
