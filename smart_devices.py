from device_interface import SmartDevice
from enums import DeviceStatus

# OBSERVER PATTERN - Concrete Observers
class SmartLight(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = DeviceStatus.OFF
    
    def update(self, status):
        self.status = status
        print(f"{self.name} received update - Status: {status.value}")
    
    def get_name(self):
        return self.name

class SmartThermostat(SmartDevice):
    def __init__(self, name):
        self.name = name
        self.status = DeviceStatus.OFF
        self.temperature = 20
    
    def update(self, status):
        self.status = status
        print(f"{self.name} received update - Status: {status.value}")
        if status == DeviceStatus.ON:
            print(f"{self.name} temperature set to {self.temperature}°C")
    
    def get_name(self):
        return self.name