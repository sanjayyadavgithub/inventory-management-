from django.db import models

# Create your models here.
class Device(models.Model):  #name of the table
    type = models.CharField(max_length=200, blank=False) #  name of the colume
    price = models.IntegerField()

    choices = (
        ('AVAILABLE','item ready to be purchased'),
        ('SOLD','item sold'),
        ('RESTOCKING','item restocking few days')
    )

    status = models.CharField(max_length=100,choices=choices, default='SOLD')
    issues = models.CharField(max_length=100, default='No issues')

    class Meta:
        abstract = False


    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type, self.price)


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass




