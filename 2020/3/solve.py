rows = open('input.txt').read().splitlines()
rows = [line.strip() for line in rows]

# You start on the open square '.' in the top-left corner.
# right 3 down 1 (for part 1, in part 2 its variable)
# Go down to the last row.
# X where there was a tree, '#'. Count how many of them there are.

def solve(right, down):
    trees = 0
    x = 0
    for y in range(down, len(rows), down):
        row = rows[y]
        x += right
        # print(x,y)
        if row[x % len(row)] == '#':
            trees += 1
            # print(row[:x-1] + 'X' + row[x+1:])
        else:
            pass
            # print(row[:x-1] + '0' + row[x+1:])
    return trees

ans = 1
for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    sol = solve(*slope)
    print(slope, sol, "<- part 1" if slope == (3, 1) else "")
    ans *= sol
print(ans)