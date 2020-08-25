from django.db import models

# Create your models here.


class Product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=30)
    category = models.CharField(max_length=50, default="")
    subCategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    publishedDate = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.productName

class Contact (models.Model):
    msgId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20,default="")
    description = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name
