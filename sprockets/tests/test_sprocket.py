import pytest
from rest_framework import status

from sprockets.models.sprocket import Sprocket
from sprockets.tests.factories.sprocket import SprocketFactory


@pytest.mark.django_db
def test_get_sprocket_then_success(api_client):
    sprocket_object = SprocketFactory()
    response = api_client.get(f"/sprockets/{sprocket_object.id}/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["outside_diameter"] == sprocket_object.outside_diameter
    assert response.data["pitch_diameter"] == sprocket_object.pitch_diameter
    assert response.data["pitch"] == sprocket_object.pitch
    assert response.data["teeth"] == sprocket_object.teeth
    assert response.data["id"] == sprocket_object.id
    assert Sprocket.objects.count() == 1


@pytest.mark.django_db
def test_get_non_existent_sprocket_then_failure(api_client):
    response = api_client.get("/sprockets/1/", format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_sprocket_then_success(api_client):
    payload = {
        "outside_diameter": 13,
        "pitch_diameter": 10,
        "pitch": 3,
        "teeth": 23,
    }
    response = api_client.post(f"/sprockets/", data=payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["outside_diameter"] == payload["outside_diameter"]
    assert response.data["pitch_diameter"] == payload["pitch_diameter"]
    assert response.data["pitch"] == payload["pitch"]
    assert response.data["teeth"] == payload["teeth"]
    assert Sprocket.objects.count() == 1


@pytest.mark.django_db
def test_create_sprocket_without_required_field_then_failure(api_client):
    payload = {
        "outside_diameter": 13,
        "pitch_diameter": 10,
        "pitch": 3,
        "teeth": 30,
    }
    del payload["outside_diameter"]

    response = api_client.post(f"/sprockets/", data=payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Sprocket.objects.count() == 0


@pytest.mark.django_db
def test_update_sprocket_then_success(api_client):
    sprocket_object = SprocketFactory()

    payload = {
        "outside_diameter": 15,
        "pitch_diameter": 15,
        "pitch": 15,
        "teeth": 30,
    }
    response = api_client.put(
        f"/sprockets/{sprocket_object.id}/", data=payload, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["outside_diameter"] == payload["outside_diameter"]
    assert response.data["pitch_diameter"] == payload["pitch_diameter"]
    assert response.data["pitch"] == payload["pitch"]
    assert response.data["teeth"] == payload["teeth"]
    assert response.data["id"] == sprocket_object.id
    assert Sprocket.objects.count() == 1


@pytest.mark.django_db
def test_update_sprocket_without_required_field_then_failure(api_client):
    sprocket_object = SprocketFactory()

    payload = {
        "outside_diameter": 13,
        "pitch_diameter": 10,
        "pitch": 3,
        "teeth": 30,
    }
    del payload["teeth"]

    response = api_client.put(
        f"/sprockets/{sprocket_object.id}", data=payload, format="json"
    )
    assert response.status_code == status.HTTP_301_MOVED_PERMANENTLY
