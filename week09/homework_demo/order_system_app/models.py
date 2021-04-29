from django.db import models

# Create your models here.

class Order(models.Model):
    product = models.CharField(max_length=50)
    number = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product