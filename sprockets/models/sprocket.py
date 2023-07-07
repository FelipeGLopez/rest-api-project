from django.db import models


class Sprocket(models.Model):
    outside_diameter = models.IntegerField(help_text="Sprocket diameter.")
    pitch_diameter = models.IntegerField(
        help_text="Pitch circle diameter of the sprocket."
    )
    pitch = models.IntegerField(
        help_text="Distance between the centers of two adjacent pins."
    )
    teeth = models.IntegerField(help_text="Number of teeth the sprocket has.")
