from django.urls import path, include
from .views import list_barbeque

urlpatterns = [
    path('', list_barbeque  , name='list_bbq'),
]
