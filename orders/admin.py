from django.contrib import admin
from .models import Orders



@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display=['size','order_status','quantity','placed_at']
    list_filter=['placed_at','order_status','size']
