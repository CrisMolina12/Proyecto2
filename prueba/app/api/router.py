from email.mime import base
from rest_framework.routers import DefaultRouter
from app.api.views import ProductoApiViewSet

router_post = DefaultRouter()
router_post.register(prefix='producto',basename='producto', viewset=ProductoApiViewSet)