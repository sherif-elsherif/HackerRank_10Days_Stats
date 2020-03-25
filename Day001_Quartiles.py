import math as m


def get_median(list):
    # calculating the median
    list.sort()  # Sorting the list
    # print(list)
    median = 0.0
    x = 0
    n_ = len(list)
    if n_ % 2 == 0:  # if we have even len, then we get the mean of the two middle values, if odd, we get the middle value
        x = int(n_ / 2)
        median = (list[x - 1] + list[x]) / 2
    else:
        x = int(m.floor(n_ / 2))
        median = list[x]
    # print(median, x)
    return median, x

n = int(input())
arr = input().split(' ')

i = 0
for item in arr:
    arr[i] = int(item)
    i += 1

q1 = q2 = q3 = 0
q2, x = get_median(arr)
q1, x1 = get_median(arr[0:x])
if n%2 ==0:
    q3, x2 = get_median(arr[x:n])
else:
    q3, x2 = get_median(arr[x+1:n])

print(int(q1))
print(int(q2))
print(int(q3))

