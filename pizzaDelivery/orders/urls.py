from django.urls import path
from PizzaDelivery.orders import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order_list_create'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_details'),
]