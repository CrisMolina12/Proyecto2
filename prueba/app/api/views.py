from rest_framework.viewsets import ModelViewSet
from app.models import  Producto
from app.api.serializers import ProductoSerializer

class ProductoApiViewSet(ModelViewSet):
    serializer_class=ProductoSerializer
    queryset= Producto.objects.all()