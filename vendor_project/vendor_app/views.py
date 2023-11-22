from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.db import models
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Vendor Profile Management:
class VendorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse({'message': 'Vendor created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
    
class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message': 'Vendor updated successfully', 'data': serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'message': 'Vendor deleted successfully'},  status=status.HTTP_204_NO_CONTENT)



# Purchase Order Tracking:
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse({'message': 'Purchase Order created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return JsonResponse({'message': 'Purchase Order updated successfully', 'data': serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'message': 'Purchase Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



# Vendor Performance Evaluation:
class VendorPerformanceView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self, request, *args, **kwargs):
        vendor = self.get_object()

        # Calculate metrics
        total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
        on_time_delivery_rate = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=models.F('acknowledgment_date')).count() / total_completed_orders * 100 if total_completed_orders > 0 else 0.0
        quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
        average_response_time = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).aggregate(Avg(models.F('acknowledgment_date') - models.F('issue_date')))['acknowledgment_date__avg'] or 0.0
        fulfillment_rate = total_completed_orders / PurchaseOrder.objects.filter(vendor=vendor).count() * 100 if PurchaseOrder.objects.filter(vendor=vendor).count() > 0 else 0.0

        # Create a new HistoricalPerformance instance
        historical_performance = HistoricalPerformance.objects.create(
            vendor=vendor,
            date=models.DateTimeField.now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )

        # Return metrics as JSON response
        serializer = HistoricalPerformanceSerializer(historical_performance)
        return JsonResponse(serializer.data)