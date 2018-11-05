from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^entry/$',views.entry,name='entry'),
    url(r'^goods/$',views.goods),
    url(r'^goods/(\d+)/$',views.goods,name='goods'),
]

