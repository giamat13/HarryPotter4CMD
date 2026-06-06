import os
import shutil
import tempfile

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________
  *      /                            \
    .   |   ✦  S C O U R G I F Y  !  |
  *      \____________________________/
     .        *    .    *       .
"""

TEMP_DIRS = [
    tempfile.gettempdir(),
    os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Temp"),
]

def clean_dir(path):
    cleaned = 0
    failed = 0
    try:
        items = os.listdir(path)
    except PermissionError:
        return 0, 0
    for item in items:
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            cleaned += 1
        except:
            failed += 1
    return cleaned, failed

def cast(*args):
    print(INTRO)
    print("  [*] Cleaning temp files...\n")
    total_cleaned = 0
    total_failed = 0
    for d in TEMP_DIRS:
        if os.path.exists(d):
            c, f = clean_dir(d)
            total_cleaned += c
            total_failed += f
            print(f"  ✦ {d}")
            print(f"      Cleaned: {c}  |  Skipped: {f}")
    print(f"\n  [*] Done. {total_cleaned} items removed, {total_failed} skipped.\n")

if __name__ == "__main__":
    cast()
