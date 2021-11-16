count = int(input())
listScore = list(map(int, input().split()))
maxScore = max(listScore)
sumScore = 0

for score in listScore:
        sumScore = sumScore + (score/maxScore*100)
avgScore = sumScore/count
print(avgScore)
