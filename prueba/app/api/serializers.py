from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from app.models import Producto


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields ='__all__'