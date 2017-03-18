'''
Wrappers for the "EAP8021X" private framework.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION = "0.1"

setup(
    name='moobjc-framework-EAP8021X',
    description="Wrappers for the private framework EAP8021X on Mac OS X",
    min_os_level='10.12',
    packages=["EAP8021X"],
    version=VERSION,
    install_requires=[
    ],
    long_description=__doc__,
)
