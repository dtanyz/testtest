from django.urls import path
from . import views

app = 'safety'

urlpatterns = [
    path('sam/', views.safety_sam, name='sam'),
]