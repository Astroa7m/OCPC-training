cases = [1211, 111, 1234, 2113, 211322, 211331122]


def bidirectional_count(num):
    def is_bidirectional(num_str):
        return num_str == num_str[::-1]

    num_str = str(num)

    count = len(num_str)

    iPointer = 0
    jPointer = len(num_str) - 1

    for _ in range(num):

        i = iPointer
        j = jPointer

        # js
        while i < j:
            if is_bidirectional(num_str[i: j + 1]):
                count += 1
            j -= 1

        i += 1
        j = jPointer
        #is
        while i < j:
            if is_bidirectional(num_str[i: j + 1]):
                count += 1
            i += 1

        jPointer -= 1
        iPointer += 1

    return count


for num in cases:
    print(f"{num} yield: {bidirectional_count(num)}")

