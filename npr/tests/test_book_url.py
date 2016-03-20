'''
Tests for the  book_to_url module
'''
from ..book_url_to_db import Saver

def test_saver():
    s = Saver()
    author, title = s._get_author_and_title('''e-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org


Title: Ulysses

Author: James Joyce

Posting Date: August 1, 2008 [EBook #4300]
Release Date: July, 2003
[Last updated: November 17, 2011]

Language: English


*** START OF THIS PROJECT GUTENBERG EBOOK ULYSSES ***

    ''')
    assert author == "James Joyce", "didnt catch correct author name %s" % author
    assert title == "Ulysses", "didnt catch correct title name %s" % title
