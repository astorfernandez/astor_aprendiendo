import os
from pathlib import Path


HOME = str(Path.home())
ROOT_PATH = os.path.join(HOME, 'tickets')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'outputs')
INPUT_PATH = os.path.join(ROOT_PATH, 'inputs')
