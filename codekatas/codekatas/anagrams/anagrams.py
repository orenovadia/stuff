from collections import defaultdict
from os.path import join, split, dirname

from codekatas.codekatas.anagrams.anagram_utils import statistics
from codekatas.codekatas.utils import timer


def _anagram_identity(s):
    return ''.join(sorted(s.replace("'", "").lower()))


def anagrams(word_iterator):
    canonic_to_anagrams = defaultdict(set)
    for word in map(str.strip, word_iterator):
        canonic_to_anagrams[_anagram_identity(word)].add(word)
    return canonic_to_anagrams


if __name__ == '__main__':
    with timer() as t:
        cta = anagrams(open(join(split(dirname(__file__))[0], 'wordlist.txt')))
        statistics(cta)
    t.inform()
