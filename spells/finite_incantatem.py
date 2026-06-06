import ctypes

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________________
  *      /                                    \
    .   |  ✦  F I N I T E  I N C A N T A T E M  !  |
  *      \____________________________________/
     .        *    .    *       .
"""

def cast(*args):
    print(INTRO)
    print("  [*] Cancelling all active curses...\n")

    # confundo - restore mouse buttons
    ctypes.windll.user32.SwapMouseButton(False)
    print("  ✦ Confundo cancelled  (mouse buttons restored)")

    # crucio - make sure cursor is visible
    while ctypes.windll.user32.ShowCursor(True) < 0:
        pass
    print("  ✦ Crucio cancelled    (cursor restored)")

    print("\n  [*] All curses lifted.\n")

if __name__ == "__main__":
    cast()
