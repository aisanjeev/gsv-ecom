from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField() 
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand_id = models.ForeignKey('Brand', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} by {self.user_id.username}"

class CartItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product_id.name} in cart"

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order_id.id}"

class Shipping(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=50)
    shipping_date = models.DateField(null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Shipping for Order {self.order_id.id}"

class CheckOut(models.Model):
    cart_id = models.ForeignKey(CartItem, on_delete=models.CASCADE ,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.TextField()
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f"Checkout for Order {self.cart_id.id}"

