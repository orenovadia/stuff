from collections import Counter
from itertools import imap
from os.path import join, split, dirname
from pprint import pprint


def statistics(canonic_to_anagrams):
    highest = max(canonic_to_anagrams.itervalues(), key=len)
    print 'Biggest Group #{} : {}'.format(len(highest), ', '.join(sorted(highest)))

    c = Counter(imap(len, canonic_to_anagrams.itervalues()))
    pprint([('Anagrams', '# groups')] + c.most_common(7))
    top_n_longest_groups = sorted(c.keys(), reverse=True)[:len(c) / 4]
    pprint([('Anagrams', '# groups')] + [(k, c[k]) for k in top_n_longest_groups])


def wordlist_open():
    return open(join(split(dirname(__file__))[0], 'wordlist.txt'))