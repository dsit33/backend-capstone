from django.test import TestCase
from restaurant.models import Booking, MenuItem

class TestMenuItem (TestCase):
    def test_str_item(self):
        item = MenuItem.objects.create(title='Ice Cream', price=5.50, inventory=100)
        self.assertEqual(str(item), 'Ice Cream : 5.50')