from django.test import TestCase
from api.models import User, Order
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class UserOrderTestecase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="testuser1", password="testpassword1")
        user2 = User.objects.create_user(username="testuser2", password="testpassword2")
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user1)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        user = User.objects.get(username="testuser1")
        self.client.force_login(user)
        response = self.client.get(reverse("user-orders"))

        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(order["user"] == user.id for order in orders))

    def test_user_order_list_unauthenticated(self):
        response = self.client.get(reverse("user-orders"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Forbidden, since user is not authenticated
