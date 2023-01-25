from __future__ import annotations
from DTPySide import *

if sys.platform=="win32":
	from .DTWindowWin32 import DTWindowWin32 as DTWindow
elif sys.platform=="linux":
	from .DTWindowLinux import DTWindowLinux as DTWindow
