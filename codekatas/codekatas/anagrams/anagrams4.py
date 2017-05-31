from collections import defaultdict

from rx import Observable
from rx.concurrency import ThreadPoolScheduler
from rx.concurrency.mainloopscheduler.asyncioscheduler import AsyncIOScheduler

from codekatas.codekatas.anagrams.anagram_utils import wordlist_open, statistics
from codekatas.codekatas.anagrams.anagrams3 import Normalizer, Anagrams, SortingCanonicalizer
from codekatas.codekatas.utils import timer


class AnagramsRx(Anagrams):
    def canonic_to_anagrams(self, word_iterator):
        d = defaultdict(set)
        o = Observable.from_iterable(word_iterator, AsyncIOScheduler()).map(self.normalizer.normalize)

        def foo(s):
            d[self.canonicalizer.canonicalize(s)].add(s)

        o.subscribe(on_next=foo)

        return d


def main(worditerable):
    d = AnagramsRx(Normalizer(), SortingCanonicalizer()).canonic_to_anagrams(worditerable)
    statistics(d)


if __name__ == '__main__':
    with timer() as t:
        main(wordlist_open())
    t.inform("functional")
