from django.urls import path
from .views import home, log_list

urlpatterns = [
    path('', home, name='home'),
    path('logs/', log_list, name='log_list'),
]