from django.urls import path
from helloworld_app import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
]
