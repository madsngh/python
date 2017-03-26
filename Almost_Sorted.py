from copy import *

def srt(a):
    b = deepcopy(a)
    b.sort()
    if a == b:
        return True
    else:
        return False

n = int(input())

arr = list(map(int, input().split(" ")))

i = -1

j = -1

for k in range(n-1):
    if arr[k] > arr[k+1]:
        i = k
        break
for l in range(n-1, 0, -1):
    if arr[l] < arr[l - 1]:
        j = l
        break



'''arr[i: j + 1][:: -1] reversing list in python'''
temp = arr[0: i] + arr[i: j + 1][:: -1] + arr[j + 1:]

temp2 = deepcopy(arr)

#swapping two no in python
temp2[i], temp2[j] = temp2[j], temp2[i]

if i == -1 and j == -1:
    print("yes")

elif srt(temp2):
    print("yes")
    print ("swap", i + 1, j + 1)

elif srt(temp):
    print ("yes")
    print ("reverse", i + 1, j + 1)
else:
    print ("no")