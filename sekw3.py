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


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
