from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcements/', views.announcements, name='announcements'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]