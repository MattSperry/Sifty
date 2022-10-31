from django.urls import path
from .views import indexPageView, aboutPageView, uploadPageView, ideasPageView

urlpatterns = [
    path('', indexPageView, name='index'),
    path('about/', aboutPageView, name='about'),
    path('upload/', uploadPageView, name='upload'),
    path('ideas/<str:fName>/<str:lName>', ideasPageView, name='ideas'),
]
