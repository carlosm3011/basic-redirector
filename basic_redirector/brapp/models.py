from django.db import models

# Create your models here.

class Urls(models.Model):
    short_code = models.CharField(max_length=25)
    destination_url = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    created_on = models.DateField()    
# end class

class Hits(models.Model):
    timestamp = models.BigIntegerField()
    short_code = models.CharField(max_length=25)
# end class

class Secrets(models.Model):
    created_on = models.DateField()
    secret = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_email = models.CharField(max_length=100)
# end class