from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Cake", price=100, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Burger", price=150, inventory=30)
    
    def test_getall(self):
        response = self.client.get(reverse('menuitems'))
        menu_items = MenuItem.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)