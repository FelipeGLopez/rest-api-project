import factory
import factory.fuzzy

from sprockets.models.sprocket import Sprocket


class SprocketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sprocket

    outside_diameter = factory.Faker("random_int", min=3, max=100)
    pitch_diameter = factory.Faker("random_int", min=2, max=100)
    pitch = factory.Faker("random_int", min=1, max=100)
    teeth = factory.Faker("random_int", min=20, max=100)
