from django.db import connection
from django.db.models import Prefetch
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryView(viewsets.ViewSet):
    """
    A SIMPLE VIEW SET FOR VIEWING CATEGORIES
    """

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        # many=True means there are more than one rows retrieving from queryset
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    """
    A SIMPLE VIEW SET FOR VIEWING CATEGORIES
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        # many=True means there are more than one rows retrieving from queryset
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A SIMPLE VIEW SET FOR VIEWING Brand
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        # many=True means there are more than one rows retrieving from queryset
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A SIMPLE VIEW SET FOR VIEWING Product
    """

    queryset = Product.objects.all().isactive()

    lookup_field = "slug"

    # def retrieve(self, request, slug=None):
    #     serializer = ProductSerializer(
    #         self.queryset.filter(slug=slug).select_related("category", "brand"),
    #         many=True,
    #     )

    #     return Response(serializer.data)
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related(Prefetch("product_line"))
            .prefetch_related(Prefetch("product_line__product_image")),
            many=True,
        )

        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        # many=True means there are more than one rows retrieving from queryset
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
    )
    def list_product_by_category_slug(self, request, slug=None):
        serializer = ProductSerializer(
            self.queryset.filter(category__slug=slug), many=True
        )
        return Response(serializer.data)
