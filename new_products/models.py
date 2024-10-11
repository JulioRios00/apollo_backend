from django.db import models

PRODUCT_CATEGORIES = [
    "portable_appliances",
    "furniture",
    "refrigerator",
    "smartphones",
    "eletronics",
]

DISCOUNTS_BY_CATEGORIES = {
    "portable_appliances": 0.05,
    "furniture": 0.03,
    "refrigerator": 0.075,
    "smartphones": 0.0255,
    "eletronics": 0.043,
}

def validate_categories(value):
    if value not in PRODUCT_CATEGORIES:
        raise ValueError("Invalid product category")

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=25)
    category = models.CharField(max_length=60, validators=[validate_categories])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def promotional_price(self):
        discount = DISCOUNTS_BY_CATEGORIES.get(self.category, 0)
        return self.price * (1 - discount)
    
    def __str__(self):
        return self.name
