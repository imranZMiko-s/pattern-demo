from abc import ABC, abstractmethod
from enums import DeviceStatus

# OBSERVER PATTERN - Observer Interface
# Abstract base class that all smart devices must implement
class SmartDevice(ABC):
    @abstractmethod
    def update(self, status: DeviceStatus):
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass