from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Order(models.Model):
    class SizeChoices(models.TextChoices):
        SMALL = 'Small'
        MEDIUM = 'Medium'
        LARGE = 'Large'
    
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        IN_TRANSIT = 'In Transit'
        DELIVERED = 'Delivered'
    
    SIZE_MAX_LENGTH = max([len(size) for _, size in SizeChoices.choices])
    STATUS_MAX_LENGTH = max([len(status) for _, status in StatusChoices.choices])

    customer = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    size = models.CharField(
        max_length=SIZE_MAX_LENGTH,
        choices=SizeChoices.choices,
        default=SizeChoices.SMALL,
    )

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    quantity = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'<Order {self.size} by {self.customer}'