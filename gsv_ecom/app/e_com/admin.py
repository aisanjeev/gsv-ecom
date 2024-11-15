from django.contrib import admin
from .models import Product, Category, Brand, Order, CartItem, Payment, Shipping, CheckOut

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'discounted_price', 'stock', 'category_id', 'brand_id', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category_id', 'brand_id', 'created_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'status', 'total_price', 'created_at', 'product_id')
    search_fields = ('user_id__username',)
    list_filter = ('status', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'quantity')
    search_fields = ('user_id__username', 'product_id__name')
    list_filter = ('user_id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'amount', 'method', 'status', 'transaction_id', 'created_at')
    search_fields = ('transaction_id',)
    list_filter = ('method', 'status', 'created_at')

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'address', 'status', 'shipping_date', 'shipping_price')
    search_fields = ('address',)
    list_filter = ('status', 'shipping_date')

@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'amount', 'coupon', 'shipping_address', 'payment_id')
    search_fields = ('cart_id','cart_id.id')
    list_filter = ('amount',)
