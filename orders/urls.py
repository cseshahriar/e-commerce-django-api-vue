from django.urls import path
from orders import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]