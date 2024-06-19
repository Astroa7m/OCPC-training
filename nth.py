def partition(arr,start, end):
    pivot = arr[start]
    i = start + 1
    j = end

    while True:
        while i <= j and arr[i] >= pivot:
            i += 1

        while j >= i and arr[j] <= pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quickSelect(arr, start, end, k):
        if start <= end:
            j = partition(arr, start, end)

            if k == j + 1:
                return arr[j]
            elif k < j + 1:
                return quickSelect(arr, start, j - 1, k)
            else:
                return quickSelect(arr, j + 1, end, k)
        else:
            return None


numberOfLists = int(input())

for i in range(numberOfLists):
    print(i+1, end=" ")
    numbers = [int(numberString) for numberString in input().split(sep=" ")]
    k = 3
    thirdLargestValue = quickSelect(numbers, 0, len(numbers)-1, k)
    print(i + 1, thirdLargestValue)