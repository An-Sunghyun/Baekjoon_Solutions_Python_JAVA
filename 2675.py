count = int(input())
result = ""

for i in range(count):
    repeat, string = input().split()
    for i in string:
        result += int(repeat) * i
    print(result)
    result = ""
