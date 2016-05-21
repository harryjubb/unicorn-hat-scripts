# https://www.raspberrypi.org/learning/robo-butler/wiimote-setup/

import cwiid
import time
import unicorntools

print 'Press 1 + 2 on your Wii Remote now...'
time.sleep(3)

# CONNECT TO THE WII REMOTE. IF IT TIMES OUT
# THEN QUIT.
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Error opening wiimote connection"
    quit()

print 'Wii Remote connected!'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
wii.led = 1

while 1:

    buttons = wii.state['buttons']
    acc = wii.state['acc']

    # IF PLUS AND MINUS BUTTONS PRESSED
    # TOGETHER THEN RUMBLE AND QUIT
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print '\nClosing connection to Wiimote...'
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)
        quit()

    unicorntools.show_all_pixels(
        acc[0],
        acc[1],
        acc[2]
    )

    time.sleep(0.01)
