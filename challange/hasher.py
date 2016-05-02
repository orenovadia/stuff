from compress import _iter_words


class Compressor(object):
    def __init__(self):
        self.m = 10240000
        self.max_bytes = 18  # approx
        a = 10**self.max_bytes
        self.k = 5
        self.mod = self.m
        self.max_hash = 10 ** 19

        self.buffer = bytearray(self.m)

    def _modulus(self, number, modulus):
        return number // 10, number % modulus

    def my_hashes(self, obj):
        h = abs(hash(obj))
        l = []
        for i in range(self.k):
            h, remainder = self._modulus(h, self.mod)
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
        print 'buffer is  %s KB' % (len(self.buffer) / 8)

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
        print "Total trail %s, false positives: %s, ratio: %s" % (
            count_all, count_miss, 1.0 * count_miss / count_all
        )


if __name__ == '__main__':
    Reader().main()
