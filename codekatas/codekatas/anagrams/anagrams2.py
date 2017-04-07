from collections import defaultdict
from itertools import imap

from stuff.codekatas.codekatas.anagrams.anagram_utils import statistics, wordlist_open
from stuff.codekatas.codekatas.utils import timer


def _anagram_identity(word):
    s = word.replace("'", "").lower()
    return sum([len(s)]+[ord(c)**2 for c in s])


def anagrams(word_iterator):
    canonic_to_anagrams = defaultdict(set)
    for word in imap(lambda s: s.strip(), word_iterator):
        canonic_to_anagrams[_anagram_identity(word)].add(word)
    return canonic_to_anagrams


if __name__ == '__main__':
    with timer() as t:
        cta = anagrams(wordlist_open())
        statistics(cta)
    t.inform()
