'''
Utils for npr project
'''
import re

import nltk
from nltk.stem.snowball import SnowballStemmer
from pymongo import MongoClient

stemmer = SnowballStemmer("english")

stopwords = nltk.corpus.stopwords.words('english')


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    stems = [stemmer.stem(t) for t in tokenize_and_stem(text)]
    return stems


def get_db_client(db_name=''):
    '''
    :param db_name:
    :return:
    '''
    # http://api.mongodb.org/python/current/faq.html#multiprocessing
    c = MongoClient()
    return c
