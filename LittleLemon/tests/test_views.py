from django.test import TestCase
from restaurant.models import Booking, MenuItem
from restaurant.views import *
from restaurant.serializers import *

class MenuViewTest (TestCase):
    def setup(self):
        item1 = MenuItem.objects.create(title='Greek Salad', price='8.00', inventory=200)
        item2 = MenuItem.objects.create(title='Chicken Quesadilla', price='6.50', inventory=400)
        item3 = MenuItem.objects.create(title='Filet Mignon', price='48.00', inventory=100)

        return MenuItemSerializer([item1, item2, item3], many=True)
    
    def test_getall(self):
        items_put = self.setup()
        items_got = MenuItemSerializer(MenuItem.objects.all(), many=True)

        for i in items_got:
            print(i)

        self.assertEqual(items_put, items_got)