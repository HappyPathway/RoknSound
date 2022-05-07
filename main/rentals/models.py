from django.db import models

# Create your models here.

class Equipment(models.Model):
    equipment_type = models.CharField(max_length=32)
    equipment_name = models.CharField(max_length=32)
    count = models.IntegerField()
    description = models.TextField()
    original_cost = models.FloatField()
    rental_rate = models.FloatField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.equipment_name

class EquipmentMedia(models.Model):
    equipment = models.ManyToManyField(Equipment)
    media = models.URLField()
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class EquipmentAccessory(Equipment):
    pass