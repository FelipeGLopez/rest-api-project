import factory
import factory.fuzzy

from sprockets.models.factory import Factory


class FactoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Factory

    name = factory.Faker("name")
