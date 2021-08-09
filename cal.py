

def draw_across_line(count):
    for i in range(count):
        if i == count-1:
            print("")
            break
        print("-", end="")
        # print(i, end="")


def draw_down_line(count, diverted_flag=''):
    for i in range(count):
        print("|", end=diverted_flag)

def calculate(i):
    result = 0
    for j in range(1, 7):
        result = i + j
        if j == 6:
            print(str(result) + " ")
        else:
            print(str(result) + " ", end="")


print(" ", end="")
for num in range(1, 7):
    draw_down_line(1)
    print(num, end='')
    if num == 6:
        draw_down_line(1)
        print("")

draw_across_line(14)

for num in range(1, 7):
    print(num, end="")
    draw_down_line(1)
    calculate(num)
