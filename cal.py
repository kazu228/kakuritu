

def draw_across_line(count):
    for i in range(count):
        if i == count-1:
            print("")
            break
        print("-", end="")
        # print(i, end="")


def draw_down_line(count):
    for i in range(count):
        print("|", end='')


for num in range(1, 7):
    draw_down_line(1)
    print(num, end='')
    if num == 6:
        draw_down_line(1)
        print("")

draw_across_line(14)

for num in range(1, 7):
    print(num)