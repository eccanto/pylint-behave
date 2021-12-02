import pylint

# pylint before version 2.3 does not support load_configuration() hook.
LOAD_CONFIGURATION_SUPPORTED = False
try:
    LOAD_CONFIGURATION_SUPPORTED = tuple(pylint.__version__.split('.')) >= ('2', '3')
except AttributeError:
    LOAD_CONFIGURATION_SUPPORTED = pylint.__pkginfo__.numversion >= (2, 3)
