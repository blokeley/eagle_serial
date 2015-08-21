"""writer.py - serial writer

Usage: python writer.py COMn
where n is the COM port number

Enter an empty line to exit
"""

import serial
import sys


BAUD = 115200 # pulses per second


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    ser = serial.Serial(sys.argv[1], BAUD)
    print('Writer connected to {}'.format(ser.name))
    print('Enter an empty line to exit.')

    prompt = '{}> '.format(ser.name)
    message = input(prompt)

    try:
        while message:
            bytez = (message + '\r').encode()
            print('{}: {}'.format(type(bytez), bytez), flush=True)
            written = ser.write(bytez)
            print('{} bytes written'.format(written))
            message = input(prompt)

    except KeyboardInterrupt:
        print('Exit OK.')

    finally:
        ser.close()
