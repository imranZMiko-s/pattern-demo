from enums import DeviceStatus

# SINGLETON PATTERN
# Purpose: Ensures only one controller exists in the system
# Use Case: Central control point for all smart devices
class SmartHomeController:
    _instance = None  # Private class variable to hold the single instance
    
    def __new__(cls):
        # Ensure only one instance is created
        if cls._instance is None:
            cls._instance = super(SmartHomeController, cls).__new__(cls)
            cls._instance._devices = []  # List of observer devices
            cls._instance._status = DeviceStatus.OFF
            print("Creating new Smart Home Controller instance")
        return cls._instance
    
    # OBSERVER PATTERN - Subject Methods
    # These methods manage the observers (devices) and notify them of changes
    def register_device(self, device):
        if device not in self._devices:
            self._devices.append(device)
            print(f"Device {device.get_name()} registered with the controller")
    
    def unregister_device(self, device):
        if device in self._devices:
            self._devices.remove(device)
            print(f"Device {device.get_name()} unregistered from the controller")
    
    def notify_all(self, status):
        self._status = status
        # Notify all observers (devices) of the state change
        for device in self._devices:
            device.update(status)
    
    def get_status(self):
        return self._status