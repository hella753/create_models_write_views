from django.db import models
from django.contrib.auth.models import User
from store.models import Category, Product


class Order(models.Model):
    AVAILABLE_STATUSES = [("P", "Pending"), ("S", "Shipped"), ("D", "Delivered")]

    order_date = models.DateField("შეკვეთის თარიღი", auto_now_add=True)
    order_status = models.CharField("სტატუსი", max_length=100, default="Pending", choices=AVAILABLE_STATUSES)
    product_id = models.ForeignKey("store.Product", on_delete=models.CASCADE, verbose_name="პროდუქტი")
    product_quantity = models.PositiveIntegerField("რაოდენობა")
    order_total = models.DecimalField("ჯამური ფასი", max_digits=10, decimal_places=2)
    order_customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="მომხმარებელი"
    )
    order_address= models.CharField(max_length=100, verbose_name="მისამართი")

    def __str__(self):
        return f"Order {self.id} | status {self.order_status}"