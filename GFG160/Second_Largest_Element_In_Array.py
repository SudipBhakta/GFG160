arr = [6,12,8,9,50,80,4,30,33,33,80]

if arr[0]>arr[1]:
    max1 = arr[0]
    max2 = arr[1]

else:
    max1 = arr[1]
    max2 = arr[0]

for i in range(2,len(arr),1):

    if arr[i]>max1:
        max2 = max1
        max1 = arr[i]

    elif arr[i] > max2 and arr[i] != max1:
        max2 = arr[i]
print(max2)