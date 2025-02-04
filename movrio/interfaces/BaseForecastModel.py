from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import random
from visualizer.models import Estimate, Place

class BaseForecastModel(ABC):
    """
    Abstract class to define the base structure of a forecast model.
    Implements the Template Method pattern with the methods: load_data(), process_data(), and evaluate_estimate().
    """

    def __init__(self, data=None, params=None):
        """
        Initializes the model with generic data and optional parameters.
        """
        self.data = data
        self.params = params if params is not None else {}

    def run_model(self) -> Estimate:
        """
        Runs the model following the Template Method:
        1. Loads the data
        2. Processes the data
        3. Evaluates and returns the estimate
        """
        self.load_data()
        self.process_data()
        return self.evaluate_estimate()

    @abstractmethod
    def load_data(self):
        """
        Abstract method to load the necessary data for the estimate.
        Must be implemented in the child classes.
        """
        pass

    @abstractmethod
    def process_data(self):
        """
        Abstract method to process the loaded data.
        Must be implemented in the child classes.
        """
        pass

    @abstractmethod
    def evaluate_estimate(self) -> Estimate:
        """
        Abstract method to generate an estimate based on the processed data.
        Must be implemented in the child classes.
        Returns an Estimate object.
        """
        pass