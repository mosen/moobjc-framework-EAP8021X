'''
Python mapping for the Security framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
'''
import sys
import objc
import CoreFoundation

from Security import _metadata

sys.modules['EAP8021X'] = mod = objc.ObjCLazyModule('EAP8021X',
    "com.apple.SystemConfiguration.EAP8021X",
    objc.pathForFramework("/System/Library/PrivateFrameworks/EAP8021X.framework"),
    _metadata.__dict__, None, {
       '__doc__': __doc__,
       '__path__': __path__,
       '__loader__': globals().get('__loader__', None),
       'objc': objc,
    }, ( CoreFoundation,))

import sys
del sys.modules['EAP8021X._metadata']
