from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view(), name="product-list"),
    path("products/info/", views.ProductInfoAPIView.as_view(), name="product-list"),
    path(
        "products/<int:product_id>/",
        views.ProductDetailAPIView.as_view(),
        name="product-list",
    ),
    path("orders/", views.OrderListAPIView.as_view(), name="order-list"),
    path("user-orders/", views.UserOrderListAPIView.as_view(), name="user-orders")
]
