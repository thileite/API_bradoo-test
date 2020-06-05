from rest_framework.viewsets import ModelViewSet
from vendors.models import Vendors
from .serializers import VendorsSerializer


class VendorsViewSet(ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializer

