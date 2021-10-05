from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(max_length=10)
    image = models.ImageField(upload_to="images/", default="images/default.png")

    def __str__(self):
        return self.title
    