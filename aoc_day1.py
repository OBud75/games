f = open("advent_of_code_day_1_input.txt", "r")
for line in f:
    lines = f.readlines()

max_sum = 0
group = list()
for line in lines:
    if line == ("\n"):
        sum_of_group = sum(int(number) for number in group)
        if sum_of_group > max_sum:
            max_sum = sum_of_group
        group = list()
    else:
        group.append(line)

print(max_sum)
