from django.urls import path
from PizzaDelivery.authentication import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]