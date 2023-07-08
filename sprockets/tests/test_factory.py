import pytest
from rest_framework import status

from sprockets.models.factory import Factory
from sprockets.tests.factories.factory import FactoryFactory


@pytest.mark.django_db
def test_get_factory_then_success(api_client):
    factory_object = FactoryFactory()
    response = api_client.get(f"/factories/{factory_object.id}/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == factory_object.name
    assert response.data["id"] == factory_object.id
    assert Factory.objects.count() == 1


@pytest.mark.django_db
def test_get_non_existent_factory_then_failure(api_client):
    response = api_client.get("/factories/1/", format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND
