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
    path('update/<int:idea_id>', updateIdeaPageView, name='update-idea'),
    path('add_info/', addInfoPageView, name='add_info'),
    path('deleteEntry/<int:idea_id>', deleteIdeaEntry, name='delete-entry'),
    path('update/update-entry-submit', updateEntry, name='update-entry-submit'),
    path('addIdea/', addIdeaPageView, name='add-idea')
]
