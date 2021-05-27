"""
This checks the battery time to time
And if its about to full & plugs in then it will start making sounds
"""


import sys
import  sched
import time
from time import sleep
import psutil


WAIT_TIME = 5*60


s = sched.scheduler(time.time, time.sleep)


def chk_battery():
    battery = psutil.sensors_battery()

    plugged = battery.power_plugged
    bet_per = battery.percent


    if plugged and bet_per > 90:
        make_beep()

    s.enter(WAIT_TIME, 1, chk_battery)


def make_beep():
    if sys.platform == 'win32':
        import winsound

        duration = 100  # milliseconds
        freq = 440  # Hz

        winsound.Beep(freq, duration); sleep(0.01)
        winsound.Beep(freq, duration); sleep(0.01)
        sleep(0.5)

        winsound.Beep(freq, duration); sleep(0.01)
        winsound.Beep(freq, duration); sleep(0.01)
        sleep(0.5)

        winsound.Beep(freq, duration); sleep(0.01)
        winsound.Beep(freq, duration); sleep(0.01)

    elif sys.platform == 'Linux':
        # TODO: Have to implement it.
        # https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes
        pass


chk_battery()
s.enter(WAIT_TIME, 1, chk_battery)
s.run()
