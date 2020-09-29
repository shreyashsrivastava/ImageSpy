from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dom, name='get_dom'),
]

