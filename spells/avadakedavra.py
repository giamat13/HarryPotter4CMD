import subprocess
import time

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |  ✦  A V A D A  K E D A V R A  !  |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast():
    print(INTRO)
    time.sleep(1)
    print("  [!!!] THE KILLING CURSE!")
    print("  [!!!] PC will shut down in 10 seconds...")
    print()
    for i in range(10, 0, -1):
        print(f"  ... {i}", flush=True)
        time.sleep(1)
    subprocess.run(
        'shutdown /s /t 0 /c "Avada Kedavra was cast. There is no coming back."',
        shell=True
    )