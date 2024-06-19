# O(n*m)
def helix(arr1, arr2):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    max_sum = 0

    while i < len(arr1) and j < len(arr2):
        intersectionFound = False
        while not intersectionFound and i < len(arr1):
            sum1 += arr1[i]
            if arr1[i] in arr2:
                intersectionFound = True
            i += 1

        intersectionFound = False

        while not intersectionFound and j < len(arr2):
            sum2 += arr2[j]
            if arr2[j] in arr1:
                intersectionFound = True
            j += 1

        max_sum += max(sum1, sum2)
        sum1 = 0
        sum2 = 0

    return max_sum


def helixImproved(arr1, arr2):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    max_sum = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            # summing arr1
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            # summing arr2
            sum2 += arr2[j]
            j += 1
        else:
            # equal
            sum1 += arr1[i]
            sum2 += arr2[j]
            max_sum += max(sum1, sum2)
            sum1 = 0
            sum2 = 0
            j += 1
            i += 1

    # add leftovers
    while i < len(arr1):
        sum1 += arr1[i]
        i += 1
    while j < len(arr2):
        sum2 += arr2[j]
        j += 1
    max_sum += max(sum1, sum2)

    return max_sum


# first = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
# second = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
# first = [13, 3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
# second = [11, 1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]
first = [4, -5, 100, 1000, 1005]
second = [3, -12, 1000, 1001]

print(helixImproved(first, second))
