from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.ImageViewSet.as_view(), name='upload'),
]

