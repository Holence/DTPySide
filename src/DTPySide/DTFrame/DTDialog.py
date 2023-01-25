from __future__ import annotations
from DTPySide import *

if sys.platform=="win32":
	from .DTDialogWin32 import DTDialogWin32 as DTDialog
elif sys.platform=="linux":
	from .DTDialogLinux import DTDialogLinux as DTDialog
