import ctypes
import sys
import os

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________
  *      /                            \
    .   |   ✦  A L O H A M O R A  !  ✦     |
  *      \____________________________/
     .        *    .    *       .
"""

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def cast(*args):
    print(INTRO)
    if is_admin():
        # כבר אדמין - פותח CMD חדש ריק
        os.system('start cmd.exe')
    else:
        # מבקש הרשאות אדמין ופותח CMD ריק
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            "cmd.exe",
            None,
            None,
            1
        )

if __name__ == "__main__":
    cast()