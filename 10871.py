import sys

inputA, inputB = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))

for num in range(inputA):
    if listA[num] < inputB:
        print(listA[num], end = " ")
