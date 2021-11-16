listNum = []
for count in range(10):
    temp = int(input())
    listNum.append(temp % 42)
listNum = set(listNum)
print(len(listNum))
