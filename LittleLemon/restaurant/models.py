from django.db import models

# Create your models here.
class Booking (models.Model):
    name = models.CharField(max_length=255)
    guests = models.SmallIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.name) + ' | ' + str(self.guests) + ' @ ' + str(self.date)
    
class MenuItem (models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return self.title + ' : ' + '{:.2f}'.format(self.price)
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.price == other.price)