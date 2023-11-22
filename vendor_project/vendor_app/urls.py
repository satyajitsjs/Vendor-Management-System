from django.urls import path
from . import views as v
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('vendors', v.VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>', v.VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase_orders', v.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>', v.PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:pk>/performance', v.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('token', obtain_auth_token, name='api_token'),
]