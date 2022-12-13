from django.db import models
from datetime import datetime, timedelta

class Customer(models.Model):
    personID = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True, default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateField(default=datetime.today, blank=True)

    def __str__(self):
        return(self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self):
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        super(Customer, self).save()

    class Meta:
        db_table = 'Customer'

class IdeaCategory(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return(self.name)

    class Meta:
        db_table = 'IdeaCategory'

# two 0..* tables, postgres automatically makes association table
        

class Idea(models.Model):
    customer = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('IdeaCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length = 30)
    description = models.TextField()
    date_added = models.DateField(default=datetime.today)

    def __str__(self):
        return(self.name)

    class Meta:
        db_table = 'Idea'
