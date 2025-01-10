from django.urls import path
from PizzaDelivery.orders import views

urlpatterns = [
    path('', views.HelloOrdersView.as_view(), name='hello_order'),
]