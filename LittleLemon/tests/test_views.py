from django.test import TestCase, Client
from restaurant.models import Booking, MenuItem
from restaurant.views import *
from restaurant.serializers import *

class MenuViewTest (TestCase):
    def setUp(self):
        MenuItem.objects.create(title='Greek Salad', price='8.00', inventory=200)
        MenuItem.objects.create(title='Chicken Quesadilla', price='6.50', inventory=400)
        MenuItem.objects.create(title='Filet Mignon', price='48.00', inventory=100)

        self.client = Client()
        self.url = '/restaurant/menu/'
    
    def test_getall(self):
        response = self.client.get(self.url)
        serialized = MenuItemSerializer(MenuItem.objects.all(), many=True).data

        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(serialized, response.json())