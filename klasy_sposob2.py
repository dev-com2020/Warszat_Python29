from collections import defaultdict

current = {'zielony': 12, 'niebieski': 3}
increments = [
    ('czerwony', 5),
    ('niebieski', 17),
    ('pomarańczowy', 9),
]


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

# counter = CountMissing()
# result = defaultdict(counter.missing, current)
# for key, amount in increments:
#     result[key] += amount
# assert counter.added == 2

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


# result, count = increment_with_report(current, increments)
# assert count == 2
