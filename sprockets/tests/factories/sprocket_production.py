from datetime import timezone

import factory
import factory.fuzzy

from sprockets.models.sprocket_production import SprocketProduction
from sprockets.tests.factories.factory import FactoryFactory
from sprockets.tests.factories.sprocket import SprocketFactory


class SprocketProductionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SprocketProduction

    actual = factory.Faker("random_int", min=20, max=100)
    goal = factory.Faker("random_int", min=20, max=100)
    datetime_produced = factory.Faker("date_time", tzinfo=timezone.utc)
    sprocket = factory.SubFactory(SprocketFactory)
    factory = factory.SubFactory(FactoryFactory)
