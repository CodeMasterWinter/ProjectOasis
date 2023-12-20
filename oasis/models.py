from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Branch(models.Model):

    name = models.CharField(max_length=255)
    pastor = models.CharField(max_length=255)
    s_pastor = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    number = PhoneNumberField(region='ZA')
    history = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):

        return self.name