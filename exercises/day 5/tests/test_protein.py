import sys
from pathlib import Path
# -------- START of inconvenient addon block --------
# This block is not necessary if you have installed your package
# using e.g. pip install -e (requires setup.py)
# or have a symbolic link in your sitepackages (my preferend way)
sys.path.append(
    str(Path(__file__).parent.parent.resolve())
)
# It make import peak_finder possible
# This is a demo hack for the course :)
# --------  END of inconvenient addon block  --------

import Protein.protein as pp

def test_y_data_builder():
    metric = {'Name': {'A': 'Alanine', 'R': 'Arginine'}, '3-letter-code': {'A': 'Ala', 'R': 'Arg'}, 'hydropathy': {'A': 1.8, 'R': -4.5}}
    y_data = pp.Protein.y_data_builder(metric)
    assert y_data == [1.8, -4.5]

def test_sliding_window():
    y_data = [2, 3, 4, 8]
    mean_list = pp.Protein.sliding_window(y_data, window_size=2)
    assert mean_list == [2.5, 6]