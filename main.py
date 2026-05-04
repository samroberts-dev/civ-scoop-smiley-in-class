"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the vendor/sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
from sad import Sad
from angry import Angry

def main():
    sadly = Sad()
    smiley = Happy()
    angwy = Angry()
    smiley.show()
    sadly.show()
    angwy.show()
    time.sleep(1)
    smiley.blink()
    sadly.blink()
    angwy.blink()
    

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

