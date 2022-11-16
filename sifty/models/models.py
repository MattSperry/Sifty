from django.db import models

class Ideas(models.Model):
    idea_name = models.CharField(max_length = 30)
    idea_description = models.TextField()
    date_added = models.DateField()
    
class Idea_Category(models.Model):
    category_name = models.CharField(max_length=30)

class Customer(models.Model):
    cust_first_name = models.CharField(max_length=30)
    cust_last_name = models.CharField(max_length=30)
    cust_email = models.CharField(max_length=30)