import math as m

# getting input from user
n = int(input())
arr = input().split(' ')
weight = input().split(' ')

i = 0
while i < n:
    arr[i] = int(arr[i])
    weight[i] = int(weight[i])
    i += 1

# calculating the mean
sum_values = 0
sum_weights = 0
i = 0
while i < n:
    sum_values += arr[i] * weight[i]
    sum_weights += weight[i]
    i += 1
mean = sum_values/sum_weights
print(round(mean, 1))