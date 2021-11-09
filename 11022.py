import sys

count = int(sys.stdin.readline())
for num in range(1, count+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #"+str(num)+":",str(a),"+",str(b),"=",(a+b))
