from django.urls import path
from brapp.views import *

urlpatterns = [
    path('r/<str:short_code>', redirect, name='redirect')
]