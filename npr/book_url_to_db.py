'''
Usage:
python book_url_to_db.py <url>
the text of the file is saved to mongodb npr.books
'''
import re
import sys

import requests

from settings import Settings
from utils.dbmgr import DbClient


class Saver(object):
    def __init__(self):
        self.db = DbClient()

    def __call__(self, url):
        self.run(url)

    def _get(self, url):
        response = requests.get(url)
        return response.status_code, response.content

    def _get_author_and_title(self, content):
        author = 'Unknown'
        title = 'Unknown'
        try:
            title = re.findall("Title\:[ \t]*(.*)", content)[0]
            author = re.findall("Author\:[ \t]*(.*)", content)[0]
        except:
            print 'Unable to parse author and title'
        print "Author %s\nTitle %s" % (author, title)
        return author, title

    def run(self, url):
        '''
        Get a content of a url (usually proj. guttenberg)
        Writes the content to tha db
        like so: dict(author=author, title=title, content=content)
        :param url: the full url (utf-8 or similar)
        :return: None
        '''
        print 'collecting %s' % url
        status_code, content = self._get(url)
        if status_code != 200:
            raise RuntimeError("not 200 code: %s \n\n %s" % (status_code, content))
        author, title = self._get_author_and_title(content)
        data = dict(author=author, title=title, content=content)
        insert_rv = self.db.insert_to_collection(Settings.db.database_name, Settings.db.collection_raw_text, data)
        print insert_rv


if __name__ == '__main__':
    s = Saver()
    s(sys.argv[1])
