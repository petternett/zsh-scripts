#!/usr/bin/python3

""" Set brightness of keyboard lights in two steps.
Code taken from the Arch wiki:
https://wiki.archlinux.org/index.php/Keyboard_backlight
"""
import dbus
import sys

def kb_light_set(delta):
    bus = dbus.SystemBus()
    kbd_backlight_proxy = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower/KbdBacklight')
    kbd_backlight = dbus.Interface(kbd_backlight_proxy, 'org.freedesktop.UPower.KbdBacklight')

    current = kbd_backlight.GetBrightness()
    maximum = kbd_backlight.GetMaxBrightness()
    new = max(0, min(current + delta, maximum))

    if 0 <= new <= maximum:
        current = new
        kbd_backlight.SetBrightness(current)

    return 100 * current / maximum

if __name__ == '__main__':
    if sys.argv[1] == "up":
        kb_light_set(1)
    elif sys.argv[1] == "down":
        kb_light_set(-1)
    else:
        print("set-kblight.py error")
        sys.exit(1)
