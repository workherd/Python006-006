from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# router = routers.DefaultRouter()
# router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('orders/', views.OrderList.as_view()),
    path('orders/create', views.OrderCreation.as_view()),
    path('orders/<int:id>/', views.OrderDetail.as_view()),
    path('orders/<int:id>/cancel', views.OrderCancellation.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)