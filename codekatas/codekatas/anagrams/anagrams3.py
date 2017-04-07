from abc import ABCMeta
from collections import defaultdict
from itertools import imap

from stuff.codekatas.codekatas.anagrams.anagram_utils import wordlist_open, statistics
from stuff.codekatas.codekatas.utils import timer


class Canonicalizer(object):
    __metaclass__ = ABCMeta

    @staticmethod
    def canonicalize(word):
        pass


class SortingCanonicalizer(Canonicalizer):
    @staticmethod
    def canonicalize(word):
        return ''.join(sorted(word.replace("'", "").lower()))


class ScoreCanonicalizer(Canonicalizer):
    @staticmethod
    def canonicalize(word):
        s = word.replace("'", "").lower()
        return sum([len(s)] + [ord(c) ** 2 for c in s])


class HashCanonicalizer(Canonicalizer):
    @staticmethod
    def canonicalize(word):
        s = word.replace("'", "").lower()
        return sum(hash(c) for c in s) + hash(len(s))


class Normalizer(object):
    @staticmethod
    def normalize(word):
        return word.strip()


class Anagrams(object):
    def __init__(self, normalizer, canonicalizer):
        super(Anagrams, self).__init__()
        self.canonicalizer = canonicalizer
        self.normalizer = normalizer

    def canonic_to_anagrams(self, word_iterator):
        canonic_to_anagrams = defaultdict(set)
        identity = self.canonicalizer.canonicalize
        for word in imap(self.normalizer.normalize, word_iterator):
            canonic_to_anagrams[identity(word)].add(word)
        return canonic_to_anagrams


if __name__ == '__main__':
    statisticsl = []
    for canonicalizer_cls in Canonicalizer.__subclasses__():
        with timer() as t:
            cta = Anagrams(Normalizer(), canonicalizer_cls()).canonic_to_anagrams(wordlist_open())
            statisticsl.append((canonicalizer_cls.__name__, cta))
        t.inform(canonicalizer_cls.__name__)

    for name, cta in statisticsl:
        print 'Statistics for {}'.format(name)
        statistics(cta)
