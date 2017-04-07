from time import time


class timer(object):
    def __init__(self):
        super(timer, self).__init__()
        self._started = None
        self._ended = None
        self.elapsed = None

    def start(self):
        self._started = time()

    def end(self):
        self._ended = time()
        self.elapsed = self._ended - self._started

    def inform(self):
        print 'Timer: %.2f [ms]' % (self.elapsed * 1000)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
