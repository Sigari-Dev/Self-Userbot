import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from symbolize import *
from converter import get_by_language
