# AOC2024 🎄

## Prerequisites

Install the requirements:

```bash
pip3 install -r requirements.txt
```

Run the bash script to create all .txt files for your inputs:

```bash
bash script.sh
```

Create a `.env` file based on `.env.example` and paste your AOC session cookie
inside. Here is how to get your session cookie:
https://github.com/wimglenn/advent-of-code-wim/issues/1.

## Usage

To execute the script for a specific day, .e.g day 1:

```
python3 aoc2024.py 1
```

It will automatically fetch the input (only the real one, not the example input)
and write it in `dayX.txt`. For the example input, you need to copy and paste it
manually in `dayX_example.txt`.

**Note that the input of the day is only available
when the puzzle becomes available, and that [input files should not be committed](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/).**
