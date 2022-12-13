from django.urls import path
from .views import *

urlpatterns = [
    path('index/', indexPageView, name='index'),
    path('register/', registerPageView, name='register'),
    path("", loginPageView, name="login"),
    path("logout", logoutPageView, name= "logout"),
    path('about/', aboutPageView, name='about'),
    path('upload/', uploadPageView, name='upload'),
    path('ideas', ideasPageView, name='ideas'),
    path('update/<str:pk>', updateIdeaPageView, name='update'),
    path('add_info/', addInfoPageView, name='add_info'),
]
