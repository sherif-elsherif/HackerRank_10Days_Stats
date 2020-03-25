import math as m

n = int(input())
str = input()
list = str.split(' ')
i = 0
for item in list:
    list[i] = int(item)
    i += 1

# calculating the mean
sum = 0
for num in list:
    sum += num
mean = sum/n
print(mean)

# calculating the median
list.sort() # Sorting the list
median = 0.0
x=0
if n%2 == 0:  # if we have even len, then we get the mean of the two middle values, if odd, we get the middle value
    x = int(n/2)
    median = (list[x-1]+list[x])/2
else:
    x = int(m.floor(n/2)+1)
    median = list[x-1]
print(median)

# calculating the mode

counts = {}  # initializing an empty Dict to hold our key, value to get the mode
for item in list:
    if counts.get(item) is None:
        counts[item] = 1
    else:
        counts[item] = counts[item] + 1
# now sorting the dict with values to get the most repeated value
for key in sorted(counts.items(), key=lambda x : x[1], reverse=True):
    print(key[0])
    break
