import sys
import json
import importlib
import importlib.util
import os
import time

SPELLS_JSON = os.path.join(os.path.dirname(__file__), "spells.json")

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def load_spells():
    with open(SPELLS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def show_help(spells):
    print_slow("\n  ✦ Harry Potter 4 CMD ✦\n")
    print("  Available spells:\n")
    for name, info in spells.items():
        args = " ".join(f"<{a}>" for a in info.get("args", []))
        print(f"    {name:<16} {args:<12}  {info['description']}")
    print()
    print("  Usage: python main.py <spell> [argument]")
    print()

def main():
    sys.path.insert(0, os.path.dirname(__file__))

    spells = load_spells()

    if len(sys.argv) < 2:
        show_help(spells)
        sys.exit(0)

    spell_name = sys.argv[1].lower().strip()
    extra_args = sys.argv[2:]

    if spell_name not in spells:
        print(f"\n  [!] Unknown spell: '{spell_name}'")
        print(f"  [?] Try: {', '.join(spells.keys())}\n")
        sys.exit(1)

    spell_info = spells[spell_name]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, spell_info["file"])
    spec = importlib.util.spec_from_file_location(spell_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.cast(*extra_args)

if __name__ == "__main__":
    main()
