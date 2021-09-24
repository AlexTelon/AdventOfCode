seats = open('input.txt').read().splitlines()

# bunch of lines with 
# FBFB.. (Forward, Back) works like binary to specify one of 128 rows.
# RLR    (Right, Left) works like binary to specify one of 8 rows.

def seat_id(row, col):
    return row * 8 + col

scores = []
for seat in seats:
    row = seat[:7]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)

    col = seat[7:]
    col = col.replace("L", "0").replace("R", "1")
    col = int(col, 2)

    scores.append(seat_id(row, col))
    # print(seat, row, col)

print("part1", max(scores))
scores = sorted(scores)

n = len(scores)
start = scores[0]
stop = scores[-1] + 1

total = sum(range(start, stop))
diff = total - sum(scores)
print("part2, (missing number is): ", diff)