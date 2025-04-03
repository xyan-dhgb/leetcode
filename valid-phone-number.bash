#!/bin/bash
# File containing the phone numbers
file="file.txt"
# Regular expression to match valid phone numbers
regex="^([0-9]{3}-[0-9]{3}-[0-9]{4})$|^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$"
# Extract valid phone numbers using grep
grep -E "$regex" "$file"