"""
Interface implementation module
"""
class Observer():
    def update(self, event_data):
        raise NotImplementedError("This method must be implemented by the concrete class")


class Publisher():
    def add_observer(self, observer):
        raise NotImplementedError("This method must be implemented by the concrete class")

    def remove_observer(self, observer):
        raise NotImplementedError("This method must be implemented by the concrete class")

    def notify_observers(self, event_data):
        raise NotImplementedError("This method must be implemented by the concrete class")