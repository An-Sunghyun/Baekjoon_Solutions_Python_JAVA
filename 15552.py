import sys

count = int(input())

for num in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
