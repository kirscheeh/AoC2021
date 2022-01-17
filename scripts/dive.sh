#!/bin/bash

x=0
y=0

while read line; do
    IFS=' ' read -ra array <<< "$line"
    if [[ ${array[0]} == "up" ]]; then
        y=$((y-array[1]))
    elif [[ ${array[0]} == "down" ]]; then
        y=$((y+array[1]))
    else
        x=$((x+array[1]))
    fi
done < $1

echo Destination Simple: $((x*y))

x=0
y=0
aim=0

while read line; do
    IFS=' ' read -ra array <<< "$line"
    if [[ ${array[0]} == "up" ]]; then
        aim=$((aim-array[1]))
    elif [[ ${array[0]} == "down" ]]; then
        aim=$((aim+array[1]))
    else
        y=$((y+aim*array[1]))
        x=$((x+array[1]))
    fi
done < $1

echo Destination Complex: $((x*y))