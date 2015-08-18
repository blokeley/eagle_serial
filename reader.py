"""writer.py - serial writer

Usage: python reader.py COMn

Type Ctrl-C to exit
"""

import serial
import sys

TIMEOUT = 1 # second


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    ser = serial.Serial(sys.argv[1])
    print('Reader connected to {}'.format(ser.name))
    ser.setTimeout(TIMEOUT)

    try:
        while True:
            received = ser.read().decode()
            print(received, end='', flush=True)

    except KeyboardInterrupt:
        print('Exit OK.')

    finally:
        ser.close()
