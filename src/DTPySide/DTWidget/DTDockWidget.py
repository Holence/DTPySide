from __future__ import annotations
from DTPySide import *

if sys.platform=="win32":
	from .DTDockWidgetWin32 import DTDockWidgetWin32 as DTDockWidget
elif sys.platform=="linux":
	from .DTDockWidgetLinux import DTDockWidgetLinux as DTDockWidget
