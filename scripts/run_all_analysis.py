import subprocess

scripts = [
    "plot_seebeck.py",
    "plot_powerfactor.py",
    "plot_lorenz.py",
    "plot_thermal_cond.py",
    "plot_carrier_concentration.py"
    "plot_zt.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])

print("All analysis completed.")
