import socket
import subprocess
import platform

INTRO = r"""
   *    .  *       .       *    .
.    *    ____________________________
  *      /                            \
    .   |  ✦  H O M E N U M  R E V E L I O  !  |
  *      \____________________________/
     .        *    .    *       .
"""

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def get_network_prefix(ip):
    parts = ip.split(".")
    return ".".join(parts[:3])

def cast(*args):
    print(INTRO)
    local_ip = get_local_ip()
    prefix = get_network_prefix(local_ip)
    print(f"  [*] Your IP: {local_ip}")
    print(f"  [*] Scanning network {prefix}.0/24...\n")

    param = "-n" if platform.system().lower() == "windows" else "-c"
    active = []
    for i in range(1, 255):
        ip = f"{prefix}.{i}"
        result = subprocess.run(
            ["ping", param, "1", "-w", "100", ip],
            capture_output=True
        )
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "unknown"
            active.append((ip, hostname))
            print(f"  ✦ {ip:<18} {hostname}")

    print(f"\n  [*] Found {len(active)} devices.")

if __name__ == "__main__":
    cast()
