import ctypes
import platform

def cast():
    """Silence the computer (mute volume)"""
    if platform.system() != "Windows":
        print("✗ Silencio only works on Windows")
        return

    try:
        # Use Windows API to mute
        from ctypes import wintypes, windll

        # KEYEVENTF_KEYUP = 0x0002
        # VK_VOLUME_MUTE = 0xAD
        windll.user32.keybd_event(0xAD, 0, 0, 0)
        print("Silencio cast! Computer is now muted.")
    except Exception as e:
        print(f"✗ Failed to cast Silencio: {e}")

if __name__ == "__main__":
    cast()
