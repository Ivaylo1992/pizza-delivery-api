from django.contrib import admin
from PizzaDelivery.orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('size', 'status', 'quantity', 'created_at')
    list_filter = ('size', 'status', 'created_at')