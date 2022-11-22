from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPageView, name='index'),
    path('register', registerPageView, name='register'),
    path('about/', aboutPageView, name='about'),
    path('upload/', uploadPageView, name='upload'),
    path('ideas/<str:pk>', ideasPageView, name='ideas'), #<str:first_name>/<str:last_name>
]
