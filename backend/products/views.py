from django.shortcuts import render
from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404


# Create your views here.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        if content is None:
            content = title
        # print(serializer.validated_data)
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not gonna use apparently
#     """

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk'


# product_list_view = ProductListAPIView.as_view()


# The function view below does the same thing as the two product_detail_view and product_list_create_view
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # List view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            # print(serializer.validated_data)
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.RetrieveAPIView,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)  # Detail view
        return self.list(request, *args, **kwargs)  # List view

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # Create view

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "This is a single view doing cool stuff"
        # print(serializer.validated_data)
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()
