from rest_framework.viewsets import ModelViewSet
from products.models import Products
from .serializers import ProductsSerializer



class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
