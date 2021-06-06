from datetime import datetime
from signal import pause

from gpiozero import DigitalInputDevice
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


def write_consumption():
    client = InfluxDBClient(url="http://influxdb:8086", org="sch8fa", token="influx-auth-token")
    write_api = client.write_api(write_options=SYNCHRONOUS)
    p = Point("gas").field("consumption", 0.01)
    write_api.write(bucket="gas", record=p)
    client.close()


# noinspection PyUnusedLocal
def next_consumption(pin):
    print("Consumption at {0}".format(datetime.now()))
    write_consumption()


def listen_to_input_events():
    sensor = DigitalInputDevice("GPIO4", pull_up=True)
    sensor.when_activated = next_consumption


if __name__ == '__main__':
    listen_to_input_events()
    print("Waiting...")
    pause()
