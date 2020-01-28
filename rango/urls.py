from django.urls import path
from rango import views, about

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about.about, name='about'),
]