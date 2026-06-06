import urllib.request
import json

INTRO = r"""
   .    .    .         .    .     .

.    .    __________________________________
  .      /                                  \
    .   |      ✦  R I D D I K U L U S  !   |
  .      \__________________________________/
     .        .    .    .       .

"""

def cast(*args):
    print(INTRO)
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        with urllib.request.urlopen(url, timeout=5) as res:
            data = json.loads(res.read().decode())
        print(f"  {data['setup']}")
        input("\n  [Press Enter for the punchline...]")
        print(f"\n  {data['punchline']} 😄\n")
    except Exception as e:
        print(f"  [!] Boggart escaped: {e}")

if __name__ == "__main__":
    cast()
