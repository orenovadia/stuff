from logging import getLogger
from time import sleep

logger = getLogger(__name__)


class Page(object):
    def __init__(self, query, source, data):
        super().__init__()
        self.query = query
        self.source = source
        self.data = data or {}

    def __repr__(self, *args, **kwargs):
        return 'Page<{}@{}>'.format(self.query, self.source)


class Emitter(object):
    def __init__(self):
        super().__init__()
        self._logger = logger.getChild('Emitter')

    def emit(self, page: Page) -> str:
        self._logger.info('Emitting page %s', page)
        return '{} {} {}'.format(page.query, page.source, page.data)


class Bringer(object):
    def __init__(self, source_name):
        super().__init__()
        self._logger = logger.getChild('Bringer[{}]'.format(source_name))
        self._source_name = source_name

    def bring(self, query):
        self._logger.info('Bringing %r from %r', query, self._source_name)
        sleep(0.3)
        return Page(query, self._source_name, {})
