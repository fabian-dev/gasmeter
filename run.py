from gpiozero import DigitalInputDevice
from signal import pause
from datetime import datetime


def next_consumption():
    print("Consumption at {0}".format(datetime.now()))


def listen_to_input_events():
    sensor = DigitalInputDevice("GPIO4")
    sensor.when_activated = next_consumption


if __name__ == '__main__':
    listen_to_input_events()
    print("Waiting...")
    pause()
