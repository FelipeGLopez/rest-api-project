import pytest
from django.core.management import call_command

from sprockets.models.factory import Factory
from sprockets.models.sprocket import Sprocket
from sprockets.models.sprocket_production import SprocketProduction


@pytest.mark.django_db
def test_populate_db_with_fixtures_then_success(db):
    call_command("populate_db_with_fixtures")
    assert Sprocket.objects.count() == 3
    assert Factory.objects.count() == 3
    assert SprocketProduction.objects.count() == 60
