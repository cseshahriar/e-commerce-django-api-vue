from django.urls import path
from orders import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('list/', views.OrderListApi.as_view(), name='order_list'),
]