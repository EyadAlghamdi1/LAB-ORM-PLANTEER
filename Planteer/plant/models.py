from django.db import models

# Create your models here.

class Plant(models.Model):
    category_options = [('Fruits', 'Fruits'),('Vegetables', 'Vegetables'),('Flowers', 'Flowers'),('Medicinal Planet', 'Medicinal Planet')]
    name = models.CharField(max_length=64)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=256,choices=category_options)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)