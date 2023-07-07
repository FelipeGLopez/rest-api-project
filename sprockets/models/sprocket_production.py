from django.db import models

from .factory import Factory
from .sprocket import Sprocket


class SprocketProduction(models.Model):
    actual = models.IntegerField(help_text="Number of sprockets produced.")
    goal = models.IntegerField(help_text="Number of sprockets to produce.")
    datetime_produced = models.DateTimeField(
        help_text="Date and time when sprockets were produced."
    )
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    sprocket = models.ForeignKey(Sprocket, on_delete=models.CASCADE)
