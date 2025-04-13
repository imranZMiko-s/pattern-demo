from device_interface import SmartDevice
from legacy_alarm import LegacyAlarmSystem
from enums import DeviceStatus

# ADAPTER PATTERN
# Purpose: Converts the legacy alarm system's interface to match the SmartDevice interface
# Use Case: Integrating old system with new smart home infrastructure
class AlarmSystemAdapter(SmartDevice):
    def __init__(self, legacy_alarm: LegacyAlarmSystem):
        self.legacy_alarm = legacy_alarm
        self.name = "Adapted Alarm System"
    
    def update(self, status):
        # Adapts the new status commands to legacy alarm methods
        if status == DeviceStatus.ON:
            self.legacy_alarm.arm_system()
        else:
            self.legacy_alarm.disarm_system()
    
    def get_name(self):
        return self.name