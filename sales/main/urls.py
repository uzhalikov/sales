from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
]
