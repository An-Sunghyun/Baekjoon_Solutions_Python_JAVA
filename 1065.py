num = int(input())
count = 0
for i in range(1,num+1):
    if i < 100:
        count += 1
    else:
        temp = list(map(int, str(i)))
        if temp[0] - temp[1] == temp[1] - temp[2]:
            count += 1
print(count)
