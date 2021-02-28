from django.shortcuts import render, reverse

# Create your views here.
from .models import Orders
from .serializers import OrderSerializer, CreateOrderSerializer
from .permissions import IsManagerOrReadOnly
from rest_framework import viewsets, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action, api_view


class OrderAPIViewSet(viewsets.ModelViewSet):
    """ 订单查看 """
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsManagerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)
    #
    # @action(detail=True, methods=['GET'])
    # def cancel(self, request, *args, **kwargs):
    #     order = self.get_object()
    #     if not order.is_effective:
    #         order.is_effective = False
    #         order.save()
    #         return Response({'status': '订单'})


class CreateOrderViewSet(viewsets.ModelViewSet):

    queryset = Orders.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsManagerOrReadOnly]

    def retrieve(self, request, pk=None):
        order = self.get_object()

        serializer = self.get_object(order)
        return Response(serializer.data)

    def list(self, request: Request, *args, **kwargs):
        return Response([])

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'orders': reverse('order_list', request=request, format=format),
#         # 'snippets': reverse('snippet-list', request=request, format=format)
#     })
