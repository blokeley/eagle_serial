"""writer.py - serial writer

Usage: python writer.py COMn
where n is the COM port number

Enter an empty line to exit
"""

import os
import serial
import sys

if '__main__' == __name__:

    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    ser = serial.Serial(sys.argv[1])
    print('Writer connected to {}'.format(ser.name))
    print('Enter an empty line to exit.')

    prompt = '{}> '.format(ser.name)
    message = input(prompt)

    try:
        while message:
            written = ser.write((message + os.linesep).encode())
            print('{} bytes written'.format(written))
            message = input(prompt)

    except KeyboardInterrupt:
        print('Exit OK.')

    finally:
        ser.close()
