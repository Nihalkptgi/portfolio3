from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('/qulification', views.qulification,name='qulification'),
    path('experince', views.experince,name='experince')
]