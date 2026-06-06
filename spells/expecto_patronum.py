import subprocess
import ctypes
import sys
import os

INTRO = r"""
   *    .  *       .       *    .  *    .
.    *    ________________________________________________
  *      /                                                \
    .   |  ✦  E X P E C T O   P A T R O N U M  !  ✦     |
  *      \________________________________________________/
     .        *    .    *       .         *    .

         "Happiness can be found even in the darkest of
          times, if one only remembers to turn on the light."
"""

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_exe_path():
    """Return the EXE path when frozen, or None when running as .py"""
    if getattr(sys, 'frozen', False):
        return sys.executable  # HP.exe
    return None

def cast(*args):
    print(INTRO)

    scan_type = args[0].lower() if args else "quick"
    valid = {"quick", "full", "custom"}
    if scan_type not in valid:
        print(f"  [!] Unknown scan type '{scan_type}'. Using 'quick'.")
        scan_type = "quick"

    scan_flags = {
        "quick":  "-Scan -ScanType 1",
        "full":   "-Scan -ScanType 2",
        "custom": "-Scan -ScanType 3",
    }

    defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"

    if not os.path.exists(defender_path):
        print("  [!] Windows Defender not found at expected path.")
        print(f"  [!] Expected: {defender_path}")
        return

    if not is_admin():
        print("  [!] A Patronus requires great power — elevating privileges...\n")
        exe = get_exe_path()
        if exe:
            # Running as EXE — re-launch HP.exe elevated with the spell args
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", exe,
                f"expecto-patronum {scan_type}",
                None, 1
            )
        else:
            # Running as .py — re-launch python elevated
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable,
                f'"{os.path.abspath(__file__)}" {scan_type}',
                None, 1
            )
        return

    print(f"  [*] Summoning your Patronus... ({scan_type} scan)\n")
    print(f"  [*] Launching Windows Defender — {scan_type.upper()} SCAN\n")

    cmd = f'"{defender_path}" {scan_flags[scan_type]}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("  ✦ The Patronus has driven away the Dementors!")
        print("  ✦ Scan completed successfully.\n")
    else:
        print("  [!] The Patronus flickered...")
        print(f"  [!] Exit code: {result.returncode}")
        if result.stdout:
            print(f"  [stdout] {result.stdout.strip()}")
        if result.stderr:
            print(f"  [stderr] {result.stderr.strip()}")
        print()

if __name__ == "__main__":
    cast(*sys.argv[1:])
