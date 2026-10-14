from django.db import models
from django.conf import settings
class wasteCategory(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Waste categories"
   
    def __str__(self):
        return self.name

class CollectionRequest(models.Model):

     STATUS_CHOICES=[
        ('pending','pending'),
        ('assigned','assigned'),
        ('collected','collected'),
        ('cancelled','cancelled'),

    ] 
     
     customer=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Collection_requests',
    )
     collector=models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.SET_NULL,
         null=True,
         blank=True,
         related_name='Assigned_pickups',
     )
     waste_category=models.ForeignKey(
        wasteCategory,
        on_delete=models.CASCADE
    )
     
     quantity=models.FloatField(help_text="Appropriate weight in kg")
     address=models.TextField()
     preferred_date=models.DateField()

   
     status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'

    )

     created_at=models.DateTimeField(auto_now_add=True)
     collected_at=models.DateTimeField(null=True, blank=True)

     class Meta:
         ordering=['-created_at']
     def __str__(self):
         return f"{self.customer} - {self.waste_category} ({self.status})"
     
     
     

# Create your models here.
