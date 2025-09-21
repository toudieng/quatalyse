from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('formations/', views.formations, name='formations'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]