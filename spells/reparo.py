import ctypes
import sys
import os

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________
  *      /                            \
    .   |   ✦  R E P A R O  !  ✦     |
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
        # כבר אדמין - פותח CMD חדש שמריץ sfc ונשאר פתוח
        os.system('start cmd.exe /C "sfc /scannow"')
    else:
        # מבקש הרשאות אדמין ופותח CMD עם sfc
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            "cmd.exe",
            '/C "sfc /scannow"',
            None,
            1
        )

if __name__ == "__main__":
    cast()