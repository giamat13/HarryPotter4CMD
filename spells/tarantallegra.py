import ctypes
import ctypes.wintypes
import time
import random

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |   ✦  T A R A N T A L L E G R A  ! |
  .      \__________________________________/
     .        .    .    .       .

"""

user32 = ctypes.windll.user32

def get_all_windows():
    windows = []
    def callback(hwnd, _):
        if user32.IsWindowVisible(hwnd) and user32.GetWindowTextLengthW(hwnd) > 0:
            windows.append(int(hwnd))
        return True
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    user32.EnumWindows(WNDENUMPROC(callback), 0)
    return windows

def cast(*args):
    print(INTRO)
    print("  [!!!] DANCING FEET CURSE!")
    print("  [!!!] Windows will dance for 10 seconds...\n")

    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)

    windows = get_all_windows()
    original_positions = {}
    for hwnd in windows:
        rect = ctypes.wintypes.RECT()
        user32.GetWindowRect(hwnd, ctypes.byref(rect))
        original_positions[hwnd] = (rect.left, rect.top)

    for i in range(10):
        for hwnd in original_positions:
            x = random.randint(0, max(0, sw - 400))
            y = random.randint(0, max(0, sh - 300))
            user32.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001 | 0x0004)
        print(f"  ... {10 - i}", flush=True)
        time.sleep(1)

    for hwnd, (x, y) in original_positions.items():
        user32.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001 | 0x0004)

    print("\n  ✦ Windows restored to original positions.\n")

if __name__ == "__main__":
    cast()
