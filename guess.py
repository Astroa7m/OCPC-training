#Probability One problem
def probabilityOne(iter, n0):
    n1 = 3 * n0
    isN1Even = n1 % 2 == 0
    n2 = (n1 / 2) if isN1Even else ((n1 + 1) / 2)
    n3 = 3 * n2
    n4 = int(n3 // 9)
    evenOrOdd = "even" if isN1Even else "odd"
    result = f"{iter}. {evenOrOdd} {n4}"
    return result


i = 1
while True:
    number = int(input())
    if number == 0:
        break
    print(probabilityOne(i, number))
    i+=1
