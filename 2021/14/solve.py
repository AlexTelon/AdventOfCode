from collections import defaultdict
from itertools import pairwise

template, rules_lines = open('input.txt').read().split("\n\n")

# Count of all letters. We will ensure to update this each iteration.
letter_count = defaultdict(int)
for c in template:
    letter_count[c] = template.count(c)

# Count of how many times each rule can be applied.
rules = dict(rule.strip().split(' -> ') for rule in rules_lines.splitlines())
rule_counts = defaultdict(int)
for a,b in pairwise(template + '_'):
    if a+b in rules:
        rule_counts[a+b] += 1

def get_ans(letter_count):
    """Help function that outputs the diff between the most and least common letter counts."""
    items = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    _, most = items[0]
    _, least = items[-1]
    return (most - least)

def apply_once(rule_counts):
    """Applies all rules once to the template. Returns a new rule_count."""
    new_counts = defaultdict(int)
    for pair, amount in rule_counts.items():
        if pair in rules:
            c = rules[pair][0]
            a, b = pair
            new_counts[a+c] += amount
            new_counts[c+b] += amount
            letter_count[c] += amount
    return new_counts

for i in range(40):
    if i == 10:
        print('p1', get_ans(letter_count))
    rule_counts = apply_once(rule_counts)

print('p2', get_ans(letter_count))