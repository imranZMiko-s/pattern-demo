import time
from smart_home_controller import SmartHomeController
from smart_devices import SmartLight, SmartThermostat
from legacy_alarm import LegacyAlarmSystem
from alarm_adapter import AlarmSystemAdapter
from enums import DeviceStatus

def main():
    # Get singleton instance of controller
    controller = SmartHomeController()
    
    # Create smart devices (observers)
    light = SmartLight("Living Room Light")
    thermostat = SmartThermostat("Main Thermostat")
    
    # Create legacy alarm and adapt it to the smart system
    legacy_alarm = LegacyAlarmSystem()
    adapted_alarm = AlarmSystemAdapter(legacy_alarm)
    
    # Register devices (observers) with controller (subject)
    controller.register_device(light)
    controller.register_device(thermostat)
    controller.register_device(adapted_alarm)
    
    while True:
        print("\nSmart Home Control Menu:")
        print("1. Turn all devices ON")
        print("2. Turn all devices OFF")
        print("3. Trigger ERROR state")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            controller.notify_all(DeviceStatus.ON)
        elif choice == "2":
            controller.notify_all(DeviceStatus.OFF)
        elif choice == "3":
            controller.notify_all(DeviceStatus.ERROR)
        elif choice == "4":
            print("Shutting down smart home system...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
