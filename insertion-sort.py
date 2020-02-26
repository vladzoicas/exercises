arr = [90, 5, 8, 3, 5, 6, 7, 12, 3, 78, 4, 5]
j=0
i=0
key=0

for j in range(1, len(arr)):
    key = arr[j]
    i = j-1
    while i >= 0 and arr[i] > key:
        arr[i+1] = arr[i]
        i = i - 1
    arr[i+1] = key

print(arr)

arr1 = [31, 41, 59, 26, 41, 58]

j=0
i=0
key=0

for j in range(1, len(arr1)):
    key = arr1[j]
    i = j-1
    while i >= 0 and arr1[i] < key:
        arr1[i+1] = arr1[i]
        i = i - 1
    arr1[i+1] = key

print(arr1)

#for j in range(len(arr1)):
#    print((arr1[-j-1]))
