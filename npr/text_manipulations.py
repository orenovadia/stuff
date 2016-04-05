import utils
from utils.dbmgr import DbClient
from settings import Settings

def main():
    c = DbClient()
    col = c.get_book_collection(Settings)
    book = col.find_one({"title":"Ulysses"})
    print book.keys()
    print book['title']
    content = book["content"]
    #content = content[8000:10000]
    allwords_stemmed= utils.tokenize_and_setem(content)
    result = col.update_one(book,{"$set":{"allwords_stemmed":allwords_stemmed}})
    print result
if __name__ == '__main__':
    main()