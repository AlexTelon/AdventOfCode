from collections import Counter
from itertools import pairwise

template, rules_lines = open('input.txt').read().split("\n\n")
rules = dict(rule.strip().split(' -> ') for rule in rules_lines.splitlines())

letter_count = Counter(template)

# Count of how many times each rule can be applied.
rule_counts = Counter(pairwise(template))

def get_ans(letter_count):
    """ ┬──┬ ︵ (╯°□°)╯︵ ┻━┻  ┬──┬ ¯\_(ツ)"""
    (_, most), *_, (_, least) = letter_count.most_common()
    return most - least

def apply_once(rule_counts):
    """Applies all rules once to the template. Returns a new rule_count."""
    new_counts = Counter()
    for (a,b), amount in rule_counts.items():
        c = rules[a+b]
        new_counts[a+c] += amount
        new_counts[c+b] += amount
        letter_count[c] += amount
    return new_counts

for _ in range(10):
    rule_counts = apply_once(rule_counts)
print('p1', get_ans(letter_count))

for _ in range(30):
    rule_counts = apply_once(rule_counts)
print('p2', get_ans(letter_count))