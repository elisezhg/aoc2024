#!/bin/bash

for (( i=1; i<=25; i++ )); do
    day=$(printf "%02d\n" $i)
    folder_name="day$day"
    mkdir "$folder_name"

    # sed -e "s/Day 1/Day $day/g" -e "s/day1/day$day/g" day01/day01.py > "$folder_name/day${day}.py"
    echo >> "$folder_name/day${day}_example.txt"
    echo >> "$folder_name/day${day}.txt"
done
