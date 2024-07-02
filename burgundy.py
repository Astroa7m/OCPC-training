def burgundy():
    i = 1
    while True:
        x = input()
        if len(x) == 1 and int(x) == 0:
            break

        n = int(x[0])
        numbers = []

        for s in x.split()[1:]:
            num = int(s)
            numbers.append(0 if num < 0 else num)

        if n > 3:
            numbers.remove(max(numbers))
            numbers.remove(min(numbers))

        print(f"{i}. {round(sum(numbers) / len(numbers))}")

        i += 1


burgundy()
