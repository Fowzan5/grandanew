from django.urls import path
from . views import *
from base import views


urlpatterns = [
    path('',views.index_page, name="index"),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('royal_park', views.rp_index, name="rp_index")
]
