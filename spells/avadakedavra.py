import subprocess
import sys

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |  ✦  A V A D A  K E D A V R A  !  |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast(*args):
    print(INTRO)
    if not args:
        print("  [!] Usage: avadakedavra <process>")
        print("  [!] Example: avadakedavra notepad.exe")
        return

    process = args[0]
    print(f"  [!!!] THE KILLING CURSE!")
    print(f"  [!!!] Killing '{process}'...\n")
    result = subprocess.run(
        f'taskkill /F /IM {process}',
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"  ✦ '{process}' has been vanquished.")
    else:
        print(f"  [!] Failed: {result.stderr.strip()}")