testCaseCount = int(input())
for count in range(testCaseCount):
    studentCount = 0
    listTestCase = list(map(int, input().split()))
    averageScore = sum(listTestCase[1:])/listTestCase[0]
    for studentScore in listTestCase[1:]:
        if studentScore > averageScore:
            studentCount += 1
    result = studentCount/listTestCase[0]*100
    print(f'{result:.3f}%')
