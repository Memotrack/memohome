from django.urls import path
from . import views

urlpatterns = [
    path('api/demo-request/', views.demo_request, name='demo_request'),
]