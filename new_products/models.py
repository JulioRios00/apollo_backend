from django.db import models
from decimal import Decimal

PRODUCT_CATEGORIES = [
    ("portable_appliances", "Eletroportáteis"),
    ("furniture", "Móveis"),
    ("refrigerator", "Geladeira"),
    ("smartphones", "Smartphones"),
    ("eletronics", "Eletrônicos"),
]

DISCOUNTS_BY_CATEGORIES = {
    "portable_appliances": 0.05,
    "furniture": 0.03,
    "refrigerator": 0.075,
    "smartphones": 0.0255,
    "eletronics": 0.043,
}

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    color = models.CharField(max_length=25)
    category = models.CharField(max_length=60, choices=PRODUCT_CATEGORIES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def promotional_price(self):
        discount = DISCOUNTS_BY_CATEGORIES.get(self.category, 0)
        return float(self.price) * (1 - discount)
    
    def save(self, *args, **kwargs):
        if isinstance(self.price, str):
            clean_price = self.price.replace(".", "").replace(",", ".")
            self.price = Decimal(clean_price)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    