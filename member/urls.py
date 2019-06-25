from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='join'),
    path('tryJoin/',views.tryJoin, name='tryJoin'),
    path('idCheck/',views.idCheck, name='idCheck'),
]