from django.urls import path
from products import views

urlpatterns = [
    path('latest', views.LatestProductsList.as_view()),
]