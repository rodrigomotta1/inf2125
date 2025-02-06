from interfaces.BaseForecastModel import BaseForecastModel
from visualizer.models import Estimate, Place
from datetime import datetime, timedelta
import random

class MockEstimateModel(BaseForecastModel):
    """
    Simple estimation model based on random values.
    """

    def load_data(self, data:Place, params):
        """
        Defines a random place for estimation.
        """
        if data:
            self.place = Place.objects.get(id=data.pk)
        else:
            self.place = Place.objects.order_by("?").first()

    def process_data(self):
        """
        Simulates data processing without changing behavior.
        """
        pass  # Just an example, can include filters or calculations

    def evaluate_estimate(self) -> Estimate:
        """
        Generates a random estimate for the selected place.
        """
        if not self.place:
            raise ValueError("No place available for estimation.")

        last_estimate = self.place.estimates.order_by("-datetime").first() # type: ignore
        new_datetime = last_estimate.datetime + timedelta(minutes=5) if last_estimate else datetime.now() + timedelta(minutes=5)

        new_amount = random.randint(10, 500)

        return Estimate.objects.create(
            place=self.place,
            datetime=new_datetime,
            amount=new_amount
        )