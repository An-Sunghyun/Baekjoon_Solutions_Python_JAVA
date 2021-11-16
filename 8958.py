count = int(input())
for number in range(count):
    score = 0
    sumScore = 0
    listQuiz = list(input())
    for i in listQuiz:
        if i == 'O':
            score += 1
            sumScore += score
        else:
            score = 0
    print(sumScore)
