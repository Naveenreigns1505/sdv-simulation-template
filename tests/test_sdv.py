from sdv_simulation import Vehicle

def test_accelerate():
    car = Vehicle(speed=50)
    assert car.accelerate(20) == "Accelerated to 70 km/h"

def test_brake():
    car = Vehicle(speed=70)
    assert car.brake(30) == "Slowed down to 40 km/h"
    assert car.brake(50) == "Slowed down to 0 km/h"

def test_monitor_battery():
    car = Vehicle(battery_level=15)
    assert car.monitor_battery() == "Warning: Low Battery! Please charge."

def test_drive():
    car = Vehicle(speed=80, battery_level=5)
    assert car.drive() == "Battery too low to drive."
