from django.urls import path
from csk.views import *

app_name='csk'
urlpatterns=[
    path('csk/',csk,name='csk'),
]