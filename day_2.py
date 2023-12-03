import re

result = 0

red_limit = 12
green_limit = 13
blue_limit = 14

def get_sum_of_cubes(line, color):
    for subline in line.split(","):
        if subline.find(color) != -1:
            return int("".join([char for char in subline if char.isdigit()]))
    return 0

with open("input.txt", "r") as input_file:
    for id, line in enumerate(input_file.readlines(), start=1):
        line_possible = True
        sets = line.split(":")[1].split(";")
        for set in sets:
            red_sum = get_sum_of_cubes(set, "red")
            if red_sum > red_limit:
                line_possible = False
                break
            green_sum = get_sum_of_cubes(set, "green")
            if green_sum > green_limit:
                line_possible = False
                break
            blue_sum = get_sum_of_cubes(set, "blue")
            if blue_sum > blue_limit:
                line_possible = False
                break
        if line_possible:       
            result += id
        
print(result)