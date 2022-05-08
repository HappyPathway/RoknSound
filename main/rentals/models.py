from django.db import models

# Create your models here.

class Equipment(models.Model):
    equipment_type = models.CharField(max_length=32)
    equipment_name = models.CharField(max_length=128)
    serial = models.CharField(null=True, max_length=64)
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


class RentalClient(models.Model):
    email = models.EmailField()
    drivers_license = models.ImageField()


class RentalAgreement(models.Model):
    client = models.ForeignKey(RentalClient, on_delete=models.CASCADE)
    package = models.ManyToManyField(Equipment)


class EquipmentAccessory(Equipment):
    pass