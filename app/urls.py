from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^register/$',views.register),
    url(r'^cart/$',views.cart),
    url(r'^entry/$',views.entry),
    url(r'^goods/$',views.goods)
]