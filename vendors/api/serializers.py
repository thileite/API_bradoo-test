from rest_framework.serializers import ModelSerializer
from vendors.models import Vendors
from products.api.serializers import ProductsSerializer


class VendorsSerializer(ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Vendors
        fields = ['id', 'name', 'cnpj', 'city', 'products']