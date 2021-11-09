import sys

count = int(sys.stdin.readline())

for num in range(1, count+1):
    temp = "*"*num
    print(temp.rjust(count))
