from django.db import models
from datetime import datetime, timedelta

class IdeaCategory(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return(self.category_name)

class Ideas(models.Model):
    idea_category = models.ForeignKey('IdeaCategory', null=True, blank=True)
    idea_name = models.CharField(max_length = 30)
    idea_description = models.TextField()
    date_added = models.DateField()

    def __str__(self):
        return(self.idea_name)

# two 0..* tables, postgres automatically makes association table

class Customer(models.Model):
    idea = models.ManyToManyField(Ideas, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, blank=True)
    date_joined = models.DateField(default=datetime.today, blank=True)

    def __str__(self):
        return(self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Customer, self).save()