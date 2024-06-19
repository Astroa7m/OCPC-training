def flat(expr):
    result = ""
    test_case = expr.replace("$", "").replace(" ", "")
    if len(test_case) == 1:
        result = test_case
    else:
        start_indices = []
        start_index = -1
        end_index = -1
        awaiting_number = 1
        i = 0
        while i < len(test_case):
            if end_index == i and not i == len(test_case) - 1:
                if result:
                    start = test_case[:start_index]
                    end = test_case[i + 1:]
                    test_case = start + result + end
                    result = ""
                end_index = -1
                if i == len(test_case):
                    start_index = start_indices.pop()
                    i = start_index

            if test_case[i] == "(":
                start_indices.append(i)
                i += 1
                continue
            if test_case[i] == ")":
                end_index = i
                if start_indices:
                    start_index = start_indices.pop()
                else:
                    break
                i = start_index + 1

            if not end_index == -1:
                if not test_case[i].isnumeric():
                    result += test_case[i]
                else:
                    n = int(test_case[i]) * awaiting_number
                    if not result == "":
                        result = result * n
                        awaiting_number = 1
                    else:
                        awaiting_number = n

            i += 1

    return result



test_cases = [
    ("w$", "w"),
    ("a$", "a"),
    ("(b 3)$", "bbb"),
    ("(c 4)$", "cccc"),
    ("(a (b c 2) 3)$", "abcbcabcbcabcbc"),
    ("(x (y (z (w 2) 3) 2) 2)$", "xyzwwzwwzwwyzwwzwwzwwxyzwwzwwzwwyzwwzwwzww"),
    ("(p (q (r 2) 3) (s (t 4) )  )$", "pqrrqrrqrrstttt"),
]

for item in test_cases:
    input, expectedOutput = item
    output = flat(input)
    matches = expectedOutput == output
    print(f"for input: {input}, expectedOutput: {expectedOutput}\noutput: {output}.\nMatches? {matches}\n")