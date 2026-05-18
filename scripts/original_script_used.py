#!/usr/bin/env python3

import subprocess
import sys
import shutil
from pathlib import Path

VASPRUN_XML = "vasprun.xml"
INTERP_MESH = 3
TEMP_RANGE = "300:1000:50"
OUTPUT_DIR = "figures"


def run(cmd, cwd="."):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=False)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    global VASPRUN_XML

    if len(sys.argv) > 1:
        VASPRUN_XML = sys.argv[1]

    vasprun_path = Path(VASPRUN_XML).resolve()

    if not vasprun_path.exists():
        print(f"vasprun.xml not found at: {vasprun_path}")
        sys.exit(1)

    work_dir = str(vasprun_path.parent)

    if shutil.which("btp2") is None:
        print("'btp2' not found in PATH. pip install BoltzTraP2")
        sys.exit(1)

    run(f"btp2 -so vasprun.xml", cwd=work_dir)
    run(f"btp2 interpolate -m {INTERP_MESH}.", cwd=work_dir)
    run(f"btp2 integrate interpolation.bt2 {TEMP_RANGE}", cwd=work_dir)
    run('btp2 plot -T -c ["xx","yy","zz"] interpolation.bt2', cwd=work_dir)
    run('btp2 plot -T -c ["xx","yy","zz"] interpolation.btj sigma', cwd=work_dir)
    run('btp2 plot -c ["xx","yy","zz"] interpolation.btj PF', cwd=work_dir)
    run('btp2 plot -c ["xyz","xx","yy","zz","xyz","xy"] interpolation.btj RH', cwd=work_dir)
    run('btp2 plot -T -c ["y","z"] interpolation.btj RH', cwd=work_dir)
    run('btp2 plot -c ["xyz"] --u interpolation.btj RH', cwd=work_dir)
    run('btp2 plot -c ["xyz"] interpolation.btj RH > RH_xyz.dat', cwd=work_dir)
    run("btp2 fermisurface interpolation.btj 0.0 -t 0.01 > fermisurface.conf", cwd=work_dir)

    out = Path(work_dir) / OUTPUT_DIR
    out.mkdir(exist_ok=True)
    for p in Path(work_dir).glob("*.png"):
        shutil.move(str(p), str(out / p.name))


if __name__ == "__main__":
    main()

