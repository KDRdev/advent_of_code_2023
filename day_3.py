import re

result = 0

with open("input.txt", "r") as input_file:
    # PART 1
    symbols_coordinates = []
    for y, line in enumerate(input_file.readlines(), start=1):
        symbols_coordinates += [(m.start(), y) for m in re.finditer(r"[^a-z0-9.]", line.strip())]
    input_file.seek(0)
    for y, line in enumerate(input_file.readlines(), start=1):
        for m in re.finditer(r"\d+", line.strip()):
            if any(
                [
                    coords for coords in symbols_coordinates if m.start()-1 <= coords[0] <= m.end() and y - 1 <= coords[1] <= y + 1
                ]
            ):
                result += int(m.group())
                
    # PART 2
    numbers = []
    numbers_coordinates = []
    for y, line in enumerate(input_file.readlines(), start=1):
        for m in re.finditer(r"\d+", line.strip()):
            numbers.append(m.group())
            numbers_coordinates.append(((m.start(), m.end()), y))
    input_file.seek(0)
    for y, line in enumerate(input_file.readlines(), start=1):
        for m in re.finditer(r"[*]", line.strip()):
            adjacent_numbers = [
                number for (number, num_coords) in zip(numbers, numbers_coordinates) if y - 1 <= num_coords[1] <= y + 1 and (num_coords[0][0] <= m.start() + 1 and num_coords[0][1] >= m.start())
            ]
            if len(adjacent_numbers) == 2:
                result += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
    
print(result)