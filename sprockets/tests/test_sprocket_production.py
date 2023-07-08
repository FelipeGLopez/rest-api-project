from datetime import datetime

import factory
import pytest
from rest_framework import status

from sprockets.models.sprocket_production import SprocketProduction
from sprockets.tests.factories.sprocket_production import SprocketProductionFactory


@pytest.mark.django_db
def test_get_all_sprocket_production_then_success(api_client):
    number_of_instances = 10
    sprocket_production_object = SprocketProductionFactory.create_batch(
        size=number_of_instances
    )

    response = api_client.get(f"/sprockets_factory/", format="json")
    assert response.status_code == status.HTTP_200_OK
    for index, sprocket_production in enumerate(response.data):
        assert sprocket_production["actual"] == sprocket_production_object[index].actual
        assert sprocket_production["goal"] == sprocket_production_object[index].goal
        assert (
            datetime.fromisoformat(sprocket_production["datetime_produced"])
            == sprocket_production_object[index].datetime_produced
        )
        assert (
            sprocket_production["factory"]
            == sprocket_production_object[index].factory.id
        )
        assert (
            sprocket_production["sprocket"]
            == sprocket_production_object[index].sprocket.id
        )

    assert SprocketProduction.objects.count() == number_of_instances


@pytest.mark.django_db
def test_get_empty_list_of_sprockets_productions_then_success(api_client):
    response = api_client.get(f"/sprockets_factory/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert SprocketProduction.objects.count() == 0
