from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('add_address',views.add_address,name="add_address"),
]
