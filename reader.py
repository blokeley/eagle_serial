"""reader.py - serial reader

Usage: python reader.py COMn

Type Ctrl-C to exit
"""

import serial
import sys


BAUD = 115200 # pulses per second
TIMEOUT = 1 # second


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    ser = serial.Serial(sys.argv[1], BAUD, timeout=TIMEOUT)
    print('Reader connected to {}'.format(ser.name))

    try:
        while True:
            received = ser.read().decode()
            print(received, end='', flush=True)

    except KeyboardInterrupt:
        print('Exit OK.')

    finally:
        ser.close()
