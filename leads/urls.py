
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_for_birthday, name='check_for_birthday'),
]
