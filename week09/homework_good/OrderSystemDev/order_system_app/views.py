from django.http.response import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from .models import Order
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import OrderSerializer

# Create your views here.
# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('product')
#     serializer_class = OrderSerializer

class OrderList(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreation(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    def get_object(self, ID):
        try:
            return Order.objects.get(id=ID)
        except Order.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=JsonResponse):
        order = self.get_object(id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class OrderCancellation(generics.DestroyAPIView):
    def get_object(self, ID):
        try:
            return Order.objects.get(id=ID)
        except Order.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        order = self.get_object(id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)