import platform
import os

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________
  *      /                            \
    .   |   ✦  R E V E L I O  !      |
  *      \____________________________/
     .        *    .    *       .
"""

def get_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024

def cast(*args):
    print(INTRO)
    print("  [*] Revealing system secrets...\n")

    # OS
    print(f"  ✦ OS        {platform.system()} {platform.release()} ({platform.version()})")
    print(f"  ✦ Machine   {platform.machine()} | {platform.processor()}")
    print(f"  ✦ Node      {platform.node()}")

    # RAM
    try:
        import ctypes
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]
        mem = MEMORYSTATUSEX()
        mem.dwLength = ctypes.sizeof(mem)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(mem))
        total = get_size(mem.ullTotalPhys)
        avail = get_size(mem.ullAvailPhys)
        used_pct = mem.dwMemoryLoad
        print(f"  ✦ RAM       {total} total | {avail} free | {used_pct}% used")
    except:
        print("  ✦ RAM       unavailable")

    # Disk
    try:
        import ctypes
        free_bytes = ctypes.c_ulonglong(0)
        total_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(
            "C:\\", None, ctypes.byref(total_bytes), ctypes.byref(free_bytes)
        )
        total = get_size(total_bytes.value)
        free = get_size(free_bytes.value)
        used = get_size(total_bytes.value - free_bytes.value)
        print(f"  ✦ Disk C:   {total} total | {free} free | {used} used")
    except:
        print("  ✦ Disk      unavailable")

    print()

if __name__ == "__main__":
    cast()
