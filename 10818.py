count = int(input())
listA = list(map(int, input().split()))
max = listA[0]
min = listA[0]

for number in listA:
    if number > max:
        max = number
    elif number< min:
        min = number
        
print(min, max)
