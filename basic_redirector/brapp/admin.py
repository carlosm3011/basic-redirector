from django.contrib import admin

from brapp.models import Url, Hit, Secret

# Register your models here.

admin.site.register(Url)
admin.site.register(Hit)
admin.site.register(Secret)