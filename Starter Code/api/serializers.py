from rest_framework import serializers
from .models import Product, Order, OrderItem, User



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "stock")

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(
        source="product.price", max_digits=10, decimal_places=2, read_only=True
    )
    
    
    class Meta:
        model = OrderItem
        fields = ("product_name","product_price", "quantity", "item_subtotal")



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name="total")
    user = serializers.CharField(source="user.username", read_only=True)
    
    
    
    def total(self, obj):
        order_items = obj.items.all()
        
        return sum(OrderItem.item_subtotal for OrderItem in order_items)

    class Meta:
        model = Order
        fields = ("order_id", "user", "created_at", "status", "items", "total_price" )	





class ProductInfoSerializer(serializers.Serializer):
    #pegar todos os produtos e acontagem o preço maximo
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    

      

