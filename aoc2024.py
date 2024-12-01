import os
import sys

from get_input import get_input

day = sys.argv[1].zfill(2)

get_input(day, 2024)

os.system(f"python3 day{day}/day{day}.py")
