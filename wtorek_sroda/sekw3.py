from collections.abc import MutableMapping
from typing import Dict

names = {
    'kot': 'mruczek',
    'pies': 'pimpek'
}
print(names)
print(list(names.values()))
print(list(names.keys()))
print(names.items())
print(names.popitem())


def my_func(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} = {v}')


votes = {
    'wydra': 1281,
    'miś polarny': 587,
    'lis': 863,
}


# def populate_ranks(votes, ranks):
#     names = list(votes.keys())
#     names.sort(key=votes.get, reverse=True)
#     for i, name in enumerate(names, 1):
#         ranks[name] = i

def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


# def get_winner(ranks):
#     for name, rank in ranks.items():
#         if rank == 1:
#             return name

# def get_winner(ranks):
#     if not isinstance(ranks, dict):
#         raise TypeError('Wymagane jest użycie typu dict')
#     return next(iter(ranks))

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


class SortedDict(MutableMapping[str, int]):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)
