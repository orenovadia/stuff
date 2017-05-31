import threading
from functools import partial
from logging import INFO, basicConfig, BASIC_FORMAT, getLogger
from time import time, sleep

from rx import Observable
from rx.concurrency.newthreadscheduler import NewThreadScheduler

from rxpydemo.rxpydemo.resources import Bringer, Emitter

logger = getLogger(__name__)


def t_factory(target, args=None):
    t = threading.Thread(target=target, args=args or [])
    logger.info("Creating thread on %s with %s", target, args)
    t.setDaemon(True)
    return t


def reactive():
    bringer_file_pair = (
        (Bringer('us'), open('us.jl', 'w')),
        (Bringer('them'), open('them.jl', 'w'))
    )
    emitter = Emitter()
    with open('queries') as queries:
        queries = Observable.from_(queries.readlines()) \
            .map(str.strip) \
            .subscribe_on(NewThreadScheduler())

        for bringer, f in bringer_file_pair:
            queries \
                .map(bringer.bring) \
                .map(emitter.emit) \
                .map(lambda s: s + '\n') \
                .subscribe(f.write, on_completed=partial(logger.info, 'Done'))

        a = queries.subscribe(partial(logger.info, 'Pushed %r'))  # suspend main thread
        logger.info("Connecting")
        logger.info("Done Connecting")

        sleep(3)


if __name__ == '__main__':
    basicConfig(level=INFO, format='%(threadName)s:' + BASIC_FORMAT)
    st = time()
    reactive()
    print(time() - st)
