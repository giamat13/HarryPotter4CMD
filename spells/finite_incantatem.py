import ctypes

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________________
  *      /                                    \
    .   |  ✦  F I N I T E  I N C A N T A T E M  !  |
  *      \____________________________________/
     .        *    .    *       .
"""

user32 = ctypes.windll.user32

def restore_windows():
    """Move all windows back to a sane grid layout"""
    windows = []
    def callback(hwnd, _):
        if user32.IsWindowVisible(hwnd) and user32.GetWindowTextLengthW(hwnd) > 0:
            windows.append(hwnd)
        return True
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    user32.EnumWindows(WNDENUMPROC(callback), 0)

    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    cols = 3
    w, h = sw // cols, sh // cols
    for i, hwnd in enumerate(windows):
        x = (i % cols) * w
        y = (i // cols) * h
        user32.SetWindowPos(hwnd, 0, x, y, 0, 0, 0x0001 | 0x0004)

def cast(*args):
    print(INTRO)
    print("  [*] Cancelling all active curses...\n")

    # confundo - restore mouse buttons
    user32.SwapMouseButton(False)
    print("  ✦ Confundo cancelled        (mouse buttons restored)")

    # crucio - restore cursor visibility
    while user32.ShowCursor(True) < 0:
        pass
    print("  ✦ Crucio cancelled          (cursor restored)")

    # tarantallegra - restore windows to grid
    restore_windows()
    print("  ✦ Tarantallegra cancelled   (windows repositioned)")

    print("\n  [*] All curses lifted.\n")

if __name__ == "__main__":
    cast()
