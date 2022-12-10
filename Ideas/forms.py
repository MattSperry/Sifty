from django import forms
from .models import Idea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user