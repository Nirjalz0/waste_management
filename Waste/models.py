from django.db import models
from django.contrib.auth.models import User
class wasteCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class collectionRequest(models.Model):
    customer=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    waste_category=models.ForeignKey(
        wasteCategory,
        on_delete=models.CASCADE
    )
    quantity=models.FloatField()
    address=models.TextField()
    preferred_date=models.DateField()

    STATUS_CHOICES=[
        ('pending','pending'),
        ('assigned','assigned'),
        ('collected','collected'),
        ('cancelled','cancelled'),

    ]
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'

    )

    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
