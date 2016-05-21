# https://www.raspberrypi.org/learning/robo-butler/wiimote-setup/

import cwiid
import time

print 'Hold down 1 + 2 on your Wii Remote now...'
time.sleep(1)

# CONNECT TO THE WII REMOTE. IF IT TIMES OUT
# THEN QUIT.
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Error opening wiimote connection"
    quit()

print 'Wii Remote connected...'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN

while 1:

    buttons = wii.state['buttons']

    # IF PLUS AND MINUS BUTTONS PRESSED
    # TOGETHER THEN RUMBLE AND QUIT
    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print '\nClosing connection to Wiimote...'
        wii.rumble = 1
        time.sleep(1)
        wii.rumble = 0
        exit(wii)
        quit()
