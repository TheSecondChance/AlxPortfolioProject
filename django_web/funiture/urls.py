from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('allDesign/', allDesign, name='allDesign')
]