from .base import *

if DEBUG == True:
    from .dev import *

if DEBUG == False:
    from .prod import *