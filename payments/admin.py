from django.contrib import admin

from .models import Payment, Gateway

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'gateway', 'price', 'status', 'phone_number', 'created_time']
    list_filter = ['status', 'package', 'gateway']
    search_fields = ['user__username', 'phone_number']

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable']
