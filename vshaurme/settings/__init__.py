from .public import *


try:
    from .local import *
except ImportError:
    print('Some settings are not installed.. please check out settings modue')

import sys
