from pyexpat import model
from turtle import update
from django.db import models

from scope_app.var import DINO_TYPE, GENDER, LOCATION_GRID

# Create your models here.z
class Park(models.Model):
    """Model definition for Park."""
    name = models.CharField(max_length=256)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Park."""

        verbose_name = 'Park'
        verbose_name_plural = 'Parks'

    def __str__(self):
        """Unicode representation of Park."""
        return str(self.name)

    def is_safe(self):
        return self.animals.filter(herbivore=False).count() == 0


class Zone(models.Model):
    last_action = models.CharField(max_length=500, blank=True, null=True)
    park = models.ForeignKey(Park, related_name="zones", default=1, on_delete=models.CASCADE)
    location = models.CharField(max_length=256, choices=LOCATION_GRID, default=1)
    dino = models.OneToOneField("Dino", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    
    
    def __str__(self):
        return str(self.location)

    class Meta:

        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'





class Dino(models.Model):
    name = models.CharField(max_length=256)
    
    park = models.ForeignKey(Park, related_name="animals", on_delete=models.SET_NULL, blank=True, null=True)
    species = models.CharField(max_length=500, choices=DINO_TYPE)
    gender = models.CharField(max_length=100, choices=GENDER, default="Male")
    digestion_period_in_hours = models.IntegerField(default=48)
    herbivore = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Dino'
        verbose_name_plural = 'Dinos'