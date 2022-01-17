#!/bin/bash
counter_lines=0
counter=0

while read line; do
    if [[ $line > $old_value ]]; then
        counter=$((counter+1))
    fi
    counter_lines=$((counter+1))
    old_value=$line
done < "$1"

echo "Task 1": $counter

counter=0
IFS=$'\n' read -d '' -r -a lines < $1
LENGTH="${#lines[@]}"
for ((i = 0; i < $LENGTH; i++)); do
    first=${lines[i]}
    second=${lines[i+1]}
    third=${lines[i+2]}
    fourth=${lines[i+3]}
    
    current=$((first+second+third))
    next=$((second+third+fourth))
    
    if [[ $current -lt $next ]]; then
        counter=$((counter+1))
    fi
    
done

echo "Task 2": $counter

