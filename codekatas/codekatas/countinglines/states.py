from enum import Enum


class States(Enum):
    START = 1
    COMMENT_BLOCK = 2
    CODE = 3
    COMMENT = 4
    COMMENT_BLOCK_AFTER_CODE = 5


class Patterns(object):
    blank = '[^\S\n]+'
    new_line = '\n'
    cb_enter = '\/\*'
    cb_exit = '\*\/'
    one_line_comment_to_end_line = '\/\/[^\n]*\n'
    string_literal = '"[^"]*?"'
