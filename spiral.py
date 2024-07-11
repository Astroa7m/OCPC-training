r = 3
c = 2


def getNextDir(dir=""):
    if dir.lower() == "right":
        return "BELOW"
    elif dir.lower() == "below":
        return "LEFT"
    elif dir.lower() == "left":
        return "ABOVE"
    else:
        return "RIGHT"


def updateCurrentLocation(row, column, dir, r=0, c=0):
    direction = dir.lower()

    if direction == 'right' or direction == 'below':
        row = row + r
        column = column + c
    else:
        row = row - r
        column = column - c

    return (row, column)


def spiral(r, c):
    currentR, currentC = (1, 0)

    dir = getNextDir()

    t = r * c

    for i in range(r):
        # column-wise
        t -= c
        currentR, currentC = updateCurrentLocation(currentR, currentC, dir, c=c)
        c -= 1

        if t == 0:
            break

        dir = getNextDir(dir)

        # row-wise
        r -= 1
        t -= r
        currentR, currentC = updateCurrentLocation(currentR, currentC, dir, r=r)
        if t == 0:
            break
        dir = getNextDir(dir)

    return f"({currentR}, {currentC}) {dir}"


i = 1

while True:
    rows_columns = input().split(sep=" ")

    rows = int(rows_columns[0])
    columns = int(rows_columns[1])

    if rows == 0 or columns == 0:
        break


    print(f"{i}. {spiral(rows, columns)}")

    i+=1


