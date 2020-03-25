import math as m

# getting input from user
n = int(input())
arr = input().split(' ')

i = 0
while i < n:
    arr[i] = int(arr[i])
    i += 1

# calculating the mean
sum_values = 0
i = 0
while i < n:
    sum_values += arr[i]
    i += 1
mean = sum_values/n

# calculate the Standard Deviation
sum = 0
i = 0
while i<n:
  sum += (arr[i]-mean)**2
  i += 1

sd = m.sqrt(sum/n)
print(round(sd, 1))
