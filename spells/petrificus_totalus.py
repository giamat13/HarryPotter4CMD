import ctypes

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________________
  *      /                                    \
    .   |  ✦  P E T R I F I C U S  T O T A L U S  !  |
  *      \____________________________________/
     .        *    .    *       .
"""

def cast(*args):
    print(INTRO)
    print("  [!!!] FULL BODY-BIND CURSE!")
    print("  [!!!] Locking screen...\n")
    ctypes.windll.user32.LockWorkStation()

if __name__ == "__main__":
    cast()
