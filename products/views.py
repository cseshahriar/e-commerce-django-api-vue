from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
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


@api_view(['POST'])
def search_api(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'products': []})
