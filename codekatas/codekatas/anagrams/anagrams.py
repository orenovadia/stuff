from collections import defaultdict, Counter
from itertools import imap
from os.path import join, split, dirname
from pprint import pprint

from stuff.codekatas.codekatas.utils import timer


def _anagram_identity(s):
    return ''.join(sorted(s.replace("'", "").lower()))


def anagrams(word_iterator):
    canonic_to_anagrams = defaultdict(set)
    for word in imap(str.strip, word_iterator):
        canonic_to_anagrams[_anagram_identity(word)].add(word)
    return canonic_to_anagrams


def statistics(canonic_to_anagrams):
    highest = max(canonic_to_anagrams.itervalues(), key=len)
    print 'Biggest Group #{} : {}'.format(len(highest), ', '.join(sorted(highest)))

    c = Counter(imap(len, canonic_to_anagrams.itervalues()))
    pprint([('Anagrams', '# groups')] + c.most_common(7))
    top_n_longest_groups = sorted(c.keys(), reverse=True)[:len(c) / 4]
    pprint([('Anagrams', '# groups')] + [(k, c[k]) for k in top_n_longest_groups])


if __name__ == '__main__':
    with timer() as t:
        cta = anagrams(open(join(split(dirname(__file__))[0], 'wordlist.txt')))
        statistics(cta)
    t.inform()
