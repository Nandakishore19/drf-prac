from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductInLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer): # If we are performing create and update, then it is good to use ModelSerializer
    owner = UserPublicSerializer(source="user", read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_product_title]
    )

    # name = serializers.CharField(source = "title",read_only=True) # To add an identical field with a different field name
    # email = serializers.EmailField(source = 'user.email', read_only = True)
    class Meta:
        model = Product
        fields = [
            "owner",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
            'public',
            'path',
            'endpoint',
        ]

    # We might be having to use custom validations within this serializer class in situations where we will be needing the request
    def create(
        self, validated_data
    ):  # The listUpdate view will execute this func if there isnt an instance, If there is an instance if will run update upon reaching the serializer.save()
        # email = validated_data.pop("email")
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):  # Should use 'get_'attribute name defined here
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
