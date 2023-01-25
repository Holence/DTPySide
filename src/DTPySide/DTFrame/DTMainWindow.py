from __future__ import annotations
from DTPySide import *

if sys.platform=="win32":
	from .DTMainWindowWin32 import DTMainWindowWin32 as DTMainWindow
elif sys.platform=="linux":
	from .DTMainWindowLinux import DTMainWindowLinux as DTMainWindow
