from logging import INFO, basicConfig, BASIC_FORMAT

from rxpydemo.rxpydemo.resources import Bringer, Emitter


def usual():
    bringer_file_pair = (
        (Bringer('us'), open('us.jl', 'w')),
        (Bringer('them'), open('them.jl', 'w'))
    )
    emitter = Emitter()

    with open('queries') as queries:
        for query in queries:
            query = query.strip()
            for bringer, f in bringer_file_pair:
                result = bringer.bring(query)
                f.write(emitter.emit(result) + '\n')


if __name__ == '__main__':
    basicConfig(level=INFO, format='%(threadName)s:' + BASIC_FORMAT)
    usual()
