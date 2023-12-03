import re

result = 0

red_limit = 12
green_limit = 13
blue_limit = 14

def get_cubes(line, color):
    for sub_line in line.split(","):
        if sub_line.find(color) != -1:
            return int("".join([char for char in sub_line if char.isdigit()]))
    return 0

with open("input.txt", "r") as input_file:
    for id, line in enumerate(input_file.readlines(), start=1):
        line_possible = True
        sets = line.split(":")[1].split(";")
        for set in sets:
            red_cubes = get_cubes(set, "red")
            if red_cubes > red_limit:
                line_possible = False
                break
            green_cubes = get_cubes(set, "green")
            if green_cubes > green_limit:
                line_possible = False
                break
            blue_cubes = get_cubes(set, "blue")
            if blue_cubes > blue_limit:
                line_possible = False
                break
        if line_possible:     
            result += id
        
print(result)