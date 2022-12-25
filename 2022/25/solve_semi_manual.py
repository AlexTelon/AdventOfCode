t = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }

def snafu_to_decimal(x: str):
    return sum([t[c] * (5 ** i) for i, c in enumerate(x.strip()[::-1])])

print(sum(snafu_to_decimal(line) for line in open('in.txt').read().splitlines()))
# here i asked wolfram for a base 5 version and then manually fixed to the snafu base with negative values.
# 12141122440024434302
# 122-12==0-01=00-0=02
ans = '122-12==0-01=00-0=02'
print(ans)
assert snafu_to_decimal(ans) == 28115957264952