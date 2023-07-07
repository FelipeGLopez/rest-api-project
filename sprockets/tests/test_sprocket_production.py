from datetime import datetime, timezone

import pytest
from rest_framework import status

from sprockets.models.factory import Factory
from sprockets.models.sprocket import Sprocket
from sprockets.models.sprocket_production import SprocketProduction


@pytest.mark.django_db(transaction=True)
def test_get_all_sprocket_production_then_success(api_client):
    factory_object = Factory.objects.create(
        id=13,
        name="Test Factory 1",
    )

    sprocket_object = Sprocket.objects.create(
        id=14,
        outside_diameter=13,
        pitch_diameter=10,
        pitch=3,
        teeth=23,
    )

    sprocket_production_object = SprocketProduction.objects.create(
        actual=23,
        goal=43,
        datetime_produced=datetime.now(timezone.utc),
        factory=factory_object,
        sprocket=sprocket_object,
    )

    response = api_client.get(f"/sprockets_factory/", format="json")
    assert response.status_code == status.HTTP_200_OK
    for sprocket_production in response.data:
        assert sprocket_production["actual"] == sprocket_production_object.actual
        assert sprocket_production["goal"] == sprocket_production_object.goal
        assert (
            datetime.fromisoformat(sprocket_production["datetime_produced"])
            == sprocket_production_object.datetime_produced
        )
        assert sprocket_production["factory"] == sprocket_production_object.factory.id
        assert sprocket_production["sprocket"] == sprocket_production_object.sprocket.id
    assert SprocketProduction.objects.count() == 1


@pytest.mark.django_db
def test_get_empty_list_of_sprockets_productions_then_success(api_client):
    response = api_client.get(f"/sprockets_factory/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert SprocketProduction.objects.count() == 0
