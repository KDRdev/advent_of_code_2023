import re

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

def get_digit_at_index(digits, index):
    keys = list(digits.keys())
    digit = digits[keys[index]]
    return digits_mapper[digit] if not digit.isdigit() else digit

def get_digit_literals_indexes_dict(line):
    matches_indexes = {}
    for digit in digits_mapper:
        indexes = [m.start() for m in re.finditer(digit, line)]
        if indexes:
            matches_indexes.update({index: digit for index in indexes})
    return matches_indexes

with open("input.txt", "r") as input_file:
    for line in input_file.readlines():
        
        # PART 1
        digits = [char for char in line if char.isdigit()]
        result += int(f"{digits[0]}{digits[-1]}")
        
        # PART 2
        if not line.isdigit():
            digit_literals_indexes_dict = get_digit_literals_indexes_dict(line)
        
        digits_indexes = {index: char for index, char in enumerate(line) if char.isdigit()}
        digits = dict(sorted({**digits_indexes, **digit_literals_indexes_dict}.items()))
        
        first_digit = get_digit_at_index(digits, 0)
        last_digit = get_digit_at_index(digits, -1)
        
        result += int(f"{first_digit}{last_digit}")
        
print(result)