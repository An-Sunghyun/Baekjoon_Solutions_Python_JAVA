inputA = int(input())
if inputA<10:
        inputA = inputA * 10
result = inputA
count = 0

while True:
    tempTwo = result // 10
    tempOne = result % 10
    tempThird = (tempTwo + tempOne)%10
    result = (tempOne*10)+tempThird
    count = count + 1
    if inputA == result:
        break

print(count)
