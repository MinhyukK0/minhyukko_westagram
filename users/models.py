from django.db import models

class User(models.Model): 
    name         = models.CharField(max_length=300)
    email        = models.CharField(max_length=300, unique=True)
    password     = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)
    etc          = models.CharField(max_length=300, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'users'