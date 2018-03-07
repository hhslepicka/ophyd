import os
import warnings


warnings.warn("This module is deprecated, use the 'cl' object "
              "at the top level instead", stacklevel=2)

__all__ = ['setup',
           'caput', 'caget',
           'get_pv',
           'pv_form',
           'thread_class']
_cl = os.environ.get('OPHYD_CONTROL_LAYER', '').lower()

if _cl == 'caproto':
    from ._caproto_shim import setup, caput, caget, get_pv, pv_form, thread_class
else:
    from ._pyepics_shim import setup, caput, caget, get_pv, pv_form, thread_class

del _cl
