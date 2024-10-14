class Vehicle:
    def __init__(self, speed=0, battery_level=100):
        self.speed = speed  # km/h
        self.battery_level = battery_level  # percentage

    def accelerate(self, increase):
        self.speed += increase
        return f"Accelerated to {self.speed} km/h"

    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        return f"Slowed down to {self.speed} km/h"

    def monitor_battery(self):
        if self.battery_level < 20:
            return "Warning: Low Battery! Please charge."
        return f"Battery level: {self.battery_level}%"

    def drive(self):
        if self.battery_level < 10:
            return "Battery too low to drive."
        elif self.speed > 120:
            return "Warning: Speeding! Slow down."
        else:
            return f"Driving at {self.speed} km/h."
