from django.contrib import admin
from .models import Vendor,PurchaseOrder,HistoricalPerformance,CustomUser

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ['name', 'vendor_code']

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_number', 'vendor', 'order_date', 'delivery_date', 'status', 'quality_rating', 'acknowledgment_date')
    search_fields = ['po_number', 'vendor__name']

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
    search_fields = ['vendor__name']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)
admin.site.register(CustomUser)