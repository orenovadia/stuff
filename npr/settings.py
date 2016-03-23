'''
Settings for npr project
'''
import os
from ConfigParser import ConfigParser


class Variable(dict):
    '''
    A group of settings in a particular subject.
    such as db
    '''

    def __setitem__(self, key, value):
        setattr(self, key, value)
        super(Variable, self).__setitem__(key, value)


class Settings(object):
    '''
    Reads settings file,
    the structure is such that each section is accessd like so:
    Settings.db.database_name
    '''

    db = Variable()

    @classmethod
    def init(cls):
        path_of_this_file = os.path.dirname(__file__)
        cfg_file = os.path.join(path_of_this_file, 'set.cfg')
        cls.cfg = ConfigParser()
        cls.cfg.read(cfg_file)
        cls._parse()

    @classmethod
    def _set_one_str_attr(cls, variable, section, attr_name):
        variable[attr_name] = cls.cfg.get(section, attr_name)

    @classmethod
    def _parse(cls):
        for key, value in cls.cfg.items("db"):
            cls.db[key] = value


Settings.init()
