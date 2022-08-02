from django.urls import path
from . import views
urlpatterns = [
    path('test',views.dispaly,name='display')
               ]