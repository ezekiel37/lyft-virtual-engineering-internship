from abc import ABC, abstractmethod
from datetime import datetime

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self ,year):
        service_threshold_date = self.last_service_date.replace(year)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
        
