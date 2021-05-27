from django.urls import path
from django.views.generic import TemplateView
from . import views

app = 'first_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name="first_app/first_app_base.html"),name="first_app_base"),
    path('testpage/', TemplateView.as_view(template_name="first_app/first_app_testpage.html"),name="first_app_testpage"),
    path('form/', views.new_view, name='form'),
    path('board/', views.gonogo_board, name='board'),
    path('loggedout/', views.log_out, name='logout_page'),
    path('opsbrief_minutes/create/', views.opsbrief_minutes_create, name='opsbrief_minutes_create'),
    path('allopsbrief_minutes/', views.opsbrief_minutes_overview, name='allopsbrief_minutes'),
    path('opsbrief_minutes/detail/<int:minutes_id>/', views.opsbrief_minutes_detailview, name='opsbrief_minutes_detailview'),
    path('minutestovet/', views.vet_minutes_view, name='vet_minutes_view'),
    path('minutestovet/<int:minutes_id>/', views.vet_minutes_detailview, name='vet_minutes_detailview'),
    path('metartaf/', views.metar_taf_view, name='metar_taf_view'),
]