import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pathlib import Path

# Robustly load 'temp_2D.txt'. The script will first look in the script's directory
# (where this file lives) and then in the current working directory. If not found
# a clear FileNotFoundError is raised with the paths that were searched.
script_dir = Path(__file__).parent
cwd = Path.cwd()
candidates = [script_dir / 'temp_2D.txt', cwd / 'temp_2D.txt']

for p in candidates:
    if p.exists():
        Temp_Map = np.loadtxt(p)
        print(f"Loaded temp_2D.txt from: {p}")
        break
else:
    raise FileNotFoundError(
        f"temp_2D.txt not found. Searched:\n  {candidates[0]}\n  {candidates[1]}\n\n"
        "Place the file in the script directory or the working directory, or pass an explicit path."
    )

print(Temp_Map)

# Example loop over Temp_Map (complete your logic here)
for i in range(len(Temp_Map)):
    for j in range(len(Temp_Map[i])):
        pass
