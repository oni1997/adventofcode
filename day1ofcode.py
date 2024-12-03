# AdventOfCode: Day 1 2024
def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

left_list = []
right_list = []

# under test.txt details gotten from https://adventofcode.com/2024/day/1/input
with open('test.txt', 'r') as file:
    for line in file:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))

# print(left_list,"oni")
# print(right_list)
total_distance = calculate_total_distance(left_list, right_list)
print(total_distance)