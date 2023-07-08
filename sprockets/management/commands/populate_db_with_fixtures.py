from datetime import datetime, timezone

from django.core.management.base import BaseCommand
from django.db import transaction

from sprockets.models.factory import Factory
from sprockets.models.sprocket import Sprocket
from sprockets.models.sprocket_production import SprocketProduction
from sprockets.utils.read_fixtures import read_fixtures


class Command(BaseCommand):
    help = "Creates Factory, Sprocket and SprocketProduction instances from json files in fixtures folder."

    def handle(self, *args, **options):
        try:
            seed_factory_data = read_fixtures("seed_factory_data.json")
            seed_sprocket_types = read_fixtures("seed_sprocket_types.json")
            with transaction.atomic():
                for index, sprocket in enumerate(seed_sprocket_types["sprockets"]):
                    sprocket_obj = Sprocket.objects.create(
                        **sprocket,
                    )
                    factory_obj = Factory.objects.create(
                        name=f"Factory number {index+1}",
                    )
                    chart_data = seed_factory_data["factories"][index]["factory"][
                        "chart_data"
                    ]
                    chart_data_quantity = len(chart_data["sprocket_production_actual"])
                    for chart_index in range(chart_data_quantity):
                        SprocketProduction.objects.create(
                            factory=factory_obj,
                            sprocket=sprocket_obj,
                            actual=chart_data["sprocket_production_actual"][
                                chart_index
                            ],
                            goal=chart_data["sprocket_production_goal"][chart_index],
                            datetime_produced=datetime.fromtimestamp(
                                int(chart_data["time"][chart_index]),
                                timezone.utc,
                            ),
                        )

                self.stdout.write(
                    self.style.SUCCESS(
                        "Factory, Sprocket and SprocketProduction instances succesfully created"
                    )
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR("Error while populating database: %s" % e)
            )
            raise e
