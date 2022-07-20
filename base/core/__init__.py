import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
print(sys.path)
from error_handler import *
from symbolize import *