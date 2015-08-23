"""responder.py - serial responder

Usage: python responder.py COMn

Type Ctrl-C to exit
"""

import serial
import sys
import time


__version__ = '0.1'

BAUD = 115200 # pulses per second
BUFFER_SIZE = 128 #  bytes
TIMEOUT = 1 # second
MOTOR_DELAY = 0.4 # seconds

# Max and min motor position in degrees
POS_MAX = 168
POS_MIN = 0

def respond(request):
    """Return a response in the format "%d %s" where %d is a signed integer
    (0 if no error, non-zero if error), and %s is the returned info string.
    """

    # Handle the standard request for device ID information
    if request.startswith('h'):
        return 'Hello\r'

    elif request.startswith('v'):
        return 'Version {}\r'.format(__version__)

    # Handle requests to move the motor
    elif request.startswith('m'):
        positions = [float(pos) for pos in request.split()[1:]]

        # If position is out of bounds, return an error
        for position in positions:
            if not POS_MIN <= position <= POS_MAX:
                return '404 Cannot reach {}\r'.format(position)

        # Else return 0 and the time taken
        time.sleep(MOTOR_DELAY)
        print('Moved to left:{}, right:{}'.format(positions[0], positions[1]))

        # Return an arbitrary time taken, based on the max position
        return '0 {:.3f}\r'.format(max(positions) / 173)

    elif request.startswith('z'):
        time.sleep(MOTOR_DELAY)
        return '0 Calibrated motors\r'

    else:
        return '400 Bad request\r'


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    ser = serial.Serial(sys.argv[1], BAUD, timeout=TIMEOUT)
    print('Responder connected to {}'.format(ser.name))

    try:
        while True:
            request = ser.read(BUFFER_SIZE)

            if request:
                print('Request: {}'.format(request))
                response = respond(request.decode().strip())
                print('Response: {}'.format(response))
                ser.write(response.encode())

    except KeyboardInterrupt:
        print('Exit OK.')

    finally:
        ser.close()
