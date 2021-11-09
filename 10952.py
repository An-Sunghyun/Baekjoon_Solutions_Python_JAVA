import sys

while True:
    inputA, inputB = map(int, sys.stdin.readline().split())
    if (inputA == 0)and(inputB == 0):
        break
    print(inputA + inputB)
