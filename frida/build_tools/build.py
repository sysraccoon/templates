#!/usr/bin/env python3

import subprocess
from pathlib import Path
from shared_utils import BASE_PATH, get_scripts_build_map

def main():
    print(f"Compile:")
    for script_path, out_path in get_scripts_build_map().items():
        print(f"{script_path} -> {out_path}")
        compile(script_path, out_path)


def compile(script_path: Path, out_path: Path):
    subprocess.run([
        "frida-compile", script_path.as_posix(), "-o", out_path.as_posix(), "-c",
    ], check=True, cwd=BASE_PATH)


if __name__ == "__main__":
    main()
