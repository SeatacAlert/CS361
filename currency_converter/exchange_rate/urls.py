# exchange_rate/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('convert/<int:amount>/<str:source_currency>/<str:target_currency>/', views.convert_currency, name='convert_currency'),
]
