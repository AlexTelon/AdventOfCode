from collections import Counter
with open('input.txt') as f:
    data = f.read()
    count = Counter(data)
    print(count['('] - count[')'])