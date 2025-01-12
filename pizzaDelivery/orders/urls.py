from django.urls import path
from PizzaDelivery.orders import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='order_list_create'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_details'),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_status'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:user_id>/orders/<int:order_id>/', views.UserOrderDetailView.as_view(), name='user_order_details'),
]