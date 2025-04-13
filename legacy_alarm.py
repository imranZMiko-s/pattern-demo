# Legacy system with incompatible interface
class LegacyAlarmSystem:
    def __init__(self):
        self.armed = False
    
    def arm_system(self):
        self.armed = True
        print("Legacy alarm system is armed")
    
    def disarm_system(self):
        self.armed = False
        print("Legacy alarm system is disarmed")
    
    def check_status(self):
        return "ARMED" if self.armed else "DISARMED"
