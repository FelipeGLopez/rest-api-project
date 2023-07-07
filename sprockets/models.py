from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=128)


class Sprocket(models.Model):
    outside_diameter = models.IntegerField(help_text="Sprocket diameter.")
    pitch_diameter = models.IntegerField(
        help_text="Pitch circle diameter of the sprocket."
    )
    pitch = models.IntegerField(
        help_text="Distance between the centers of two adjacent pins."
    )
    teeth = models.IntegerField(help_text="Number of teeth the sprocket has.")


class SprocketProduction(models.Model):
    actual = models.IntegerField(help_text="Number of sprockets produced.")
    goal = models.IntegerField(help_text="Number of sprockets to produce.")
    datetime_produced = models.DateTimeField(
        help_text="Date and time when sprockets were produced."
    )
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    sprocket = models.ForeignKey(Sprocket, on_delete=models.CASCADE)
