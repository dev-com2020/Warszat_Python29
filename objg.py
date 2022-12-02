from collections import Counter

import objgraph

# print(objgraph.show_most_common_types())


def graph_ref(*objects):
    objgraph.show_refs(objects, filename='show.png', refcounts=True, too_many=5,
                       filter=lambda x: not isinstance(x, dict))
    objgraph.show_backrefs(objects, filename='showb.png', refcounts=True)


if __name__ == '__main__':
    quote = '''
    People who think they know everything are a
    great annoyance to those of us who do.
    '''
    words = quote.lower().strip().split()
    counts = Counter(words)
    graph_ref(words, quote, counts)
