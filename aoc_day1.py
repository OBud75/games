with open ("advent_of_code_day_1_input.txt", "r") as f:
    for line in f:
        lines = f.readlines()

current_group = list()
top_3 = list()

for line in lines:
    if line != ("\n"):
        current_group.append(line)
        continue

    sum_of_current_group = sum(int(number) for number in current_group)
    if len(top_3) < 3:
        top_3.append(sum_of_current_group)

    elif sum_of_current_group > min(top_3):
        top_3.remove(min(top_3))

    if sum_of_current_group >= min(top_3):
        top_3.append(sum_of_current_group)

    current_group = list()

print(sum(top_3))
