from django.urls import path
from . views import *
from base import views


urlpatterns = [
    path('',views.index_page, name="index"),
    path('request_form/',views.index_page),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('royal_park', views.rp_index, name="rp_index"),
    path('royal_park/request_form', views.rp_index, name="rp_index"),
    path('thanks/',views.thanks, name="thanks"),
    path('thanks/rp/',views.thanks, name="thanks")

]
