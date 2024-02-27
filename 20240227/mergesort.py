# merge sort

arr1 = [-9, 1, 6, 8, 12]
arr2 = [-7, 7, 13, 15]

sorted = []
while True:
    if not arr1 and not arr2:
        break
    if not arr1:
        sorted.append(arr2[0])
        arr2.pop(0)
        continue
    if not arr2:
        sorted.append(arr1[0])
        arr1.pop(0)
        continue
    elif arr1[0] < arr2[0]:
        sorted.append(arr1[0])
        arr1.pop(0)
    elif arr1[0] > arr2[0]:
        sorted.append(arr2[0])
        arr2.pop(0)

print(sorted)