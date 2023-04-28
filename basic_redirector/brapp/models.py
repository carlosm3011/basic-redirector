from django.db import models

# Create your models here.

class Url(models.Model):
    short_code = models.CharField(max_length=25)
    destination_url = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    created_on = models.DateField()    
    #
    def __str__(self):
        return f"short_code = {self.short_code}, destination = {self.destination_url}"
# end class

class Hit(models.Model):
    timestamp = models.BigIntegerField()
    short_code = models.CharField(max_length=25)
    #
    def __str__(self):
        return f"Hit on short code {self.short_code}"
# end class

class Secret(models.Model):
    created_on = models.DateField()
    secret = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_email = models.CharField(max_length=100)
# end class