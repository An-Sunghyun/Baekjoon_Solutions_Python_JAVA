num_array = set(range(1, 10001));
result = set()

for constructor in range(1, 10001):
    for temp in str(constructor):
        constructor += int(temp)
    result.add(constructor)    
self_number = sorted(num_array - result)
for i in self_number:
    print(i)
