import os
import subprocess

import requests
from dotenv import load_dotenv

load_dotenv()

warning = "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available."


def get_input(day, year):
    with open(f"day{day}/day{day}.txt", "r+") as f:
        # if file is empty
        file_content = f.read().strip()
        if not file_content:
            print("Fetching input...")
            res = requests.get(
                f"https://adventofcode.com/{year}/day/{int(day)}/input",
                cookies={"session": os.getenv("SESSION")},
            )

            if (res.text[:-1]) != warning:
                print("Input fetched")
                f.seek(0)
                f.write(res.text[:-1])  # remove '\n' at the end
            else:
                print("Input not yet available:", warning)
        else:
            print("hi")
