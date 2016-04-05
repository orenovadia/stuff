import utils
from utils.dbmgr import DbClient
from settings import Settings
from sklearn.feature_extraction import text
def main():
    c = DbClient()
    col = c.get_book_collection(Settings)
    print col
    book = col.find_one()
    print book.keys()
    print book['title']
    content = book['content'][2**17:2**18]
    t = text.CountVectorizer(content)
    analyzer =  t.build_analyzer()
    tokener = t.build_tokenizer()
    print t.decode(content)
    print t.get_stop_words()
if __name__ == '__main__':
    main()