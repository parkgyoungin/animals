from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='join'),
    path('tryJoin/',views.tryJoin, name='tryJoin'),
    path('idCheck/',views.idCheck, name='idCheck'),
    path('login/', views.login, name='login'),
    path("completeJoin/", views.test, name='test'),
]