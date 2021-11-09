while True:
    try:
        inputA, inputB = map(int, input().split())
        print(inputA+inputB)
    except EOFError:
        break
