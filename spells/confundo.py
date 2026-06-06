import ctypes
import time

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |      ✦  C O N F U N D O  !        |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast(*args):
    print(INTRO)
    print("  [!!!] Swapping mouse buttons for 10 seconds...\n")
    ctypes.windll.user32.SwapMouseButton(True)
    for i in range(10, 0, -1):
        print(f"  ... {i}", flush=True)
        time.sleep(1)
    ctypes.windll.user32.SwapMouseButton(False)
    print("\n  ✦ Mouse buttons restored.\n")

if __name__ == "__main__":
    cast()
