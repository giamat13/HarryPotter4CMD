import ctypes
import time
import random

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |      ✦  C R U C I O  !            |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast(*args):
    print(INTRO)
    print("  [!!!] THE CRUCIATUS CURSE!")
    print("  [!!!] Torturing mouse for 30 seconds...\n")

    user32 = ctypes.windll.user32
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)

    for i in range(30):
        x = random.randint(0, sw)
        y = random.randint(0, sh)
        user32.SetCursorPos(x, y)
        print(f"  ... {30 - i}", flush=True)
        time.sleep(0.1)

    print("\n  ✦ The curse has lifted.\n")

if __name__ == "__main__":
    cast()
