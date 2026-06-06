import ctypes
import platform
import time

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |      ✦  S O N O R U S  !   |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast():
    """Increase volume to maximum"""
    print(INTRO)

    if platform.system() != "Windows":
        print("✗ Sonorus only works on Windows")
        return

    try:
        from ctypes import windll

        # Unmute first if muted
        windll.user32.keybd_event(0xAD, 0, 0, 0)
        time.sleep(0.1)

        # Increase volume to max (press volume up 50 times)
        for _ in range(50):
            windll.user32.keybd_event(0xAF, 0, 0, 0)
            time.sleep(0.02)

        print("Sonorus cast! Volume set to maximum.")
    except Exception as e:
        print(f"✗ Failed to cast Sonorus: {e}")

if __name__ == "__main__":
    cast()
