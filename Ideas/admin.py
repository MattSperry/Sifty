from django.contrib import admin
from .models import IdeaCategory, Idea, Customer

# Register your models here.
admin.site.register(IdeaCategory)
admin.site.register(Idea)
admin.site.register(Customer)