from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer, CategorySerializer

class LatestProductsList(APIView):

    def get(self, request, fromat=None):
        products = Product.objects.all()[0:4]
        serialize = ProductSerializer(products, many=True)
        return Response(serialize.data) 


class ProductDetail(APIView):

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(
                category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, category_slug, product_slug, fromat=None):
        product = self.get_object(category_slug, product_slug)
        serialize = ProductSerializer(product)
        return Response(serialize.data)


class CategoryDetailView(APIView):

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, fromat=None):
        category = self.get_object(category_slug)
        serialize = CategorySerializer(category)
        return Response(serialize.data)
