from django.urls import path
from urlshortener import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('success/', views.success, name='success'),
]
