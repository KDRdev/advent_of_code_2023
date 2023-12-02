from operator import indexOf
from re import match


result = 0

digits_mapper = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        # PART 1
        digits = [char for char in line if char.isdigit()]
        result += int(f"{digits[0]}{digits[-1]}")
        # PART 2
        matches_indexes = {}
        if not line.isdigit():
            for digit in digits_mapper:
                if line.find(digit) != -1:
                    matches_indexes[line.find(digit)] = digit
            sorted_matches_indexes = sorted(matches_indexes)
            for index in sorted_matches_indexes:
                digit = matches_indexes[index]
                line = line.replace(digit, digits_mapper[digit])
        digits = [char for char in line if char.isdigit()]
        result += int(f"{digits[0]}{digits[-1]}")
        
print(result)