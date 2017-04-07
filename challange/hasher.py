from compress import _iter_words
import math

class Compressor(object):
    def __init__(self):
        self.n = 66000
        self.m = 400*8000#self.n * 8

        self.k = 4#int(0.7*self.m/self.n)/3
        self.divisor = 10#int(math.log(self.m, self.k))
        print 'm=',self.m, 'k=',self.k, 'divisor=',self.divisor

        self.buffer = bytearray(self.m)

    def _modulus(self, number, modulus):
        return number // self.divisor, number % modulus

    def my_hashes(self, obj):
        h = abs(hash(obj))
        l = []
        for i in range(self.k):
            h, remainder = self._modulus(h, self.m)
            l.append(remainder)
        return l

    def my_hash(self, word):
        print self.my_hashes(word)

    def hash_word(self, word):
        l = self.my_hashes(word)
        for i in l:
            self.buffer[i] = 1

    def show_buffer(self):
        s = sum(self.buffer)
        print 'buffer length %sbits buffer filled %s ratio %s' % (
            len(self.buffer), s, 1.0 * s / len(self.buffer)
        )
        print 'buffer is  %s KB' % (len(self.buffer) / 8000)

    def word_in_dictionary(self, word):
        return all(self.buffer[i] == 1 for i in self.my_hashes(word))

    def build_buffer(self):
        for word in _iter_words():
            self.hash_word(word)


class Reader(object):
    def main(self):
        c = Compressor()
        c.build_buffer()
        # for word in _iter_words():
        #     c.hash_word(word)
        c.show_buffer()
        print 'all true positives: ', all(c.word_in_dictionary(word) for word in _iter_words())
        count_hit = 0
        count_miss = 0
        count_all = 0
        for word in _iter_words('bad_words'):
            if c.word_in_dictionary(word):
                count_miss += 1
            count_all += 1
        print "Total tests %s, false positives: %s, ratio: %s" % (
            count_all, count_miss, 1.0 * count_miss / count_all
        )


if __name__ == '__main__':
    Reader().main()
