from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<work_id>', views.delete, name="delete"),
    path('cross_off/<work_id>', views.cross_off, name="cross_off"),
    path('uncross/<work_id>', views.uncross, name="uncross"),
    path('edit/<work_id>', views.edit, name="edit"),
]
