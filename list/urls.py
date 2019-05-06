from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),

]
urlpatterns += [
     path('start', views.index, name="order")
]
urlpatterns += [
     path('order', views.order, name="order")
]
urlpatterns += [
     path('product', views.product, name="product")
]

