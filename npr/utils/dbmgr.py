'''
Arbitrator for the db used
should have similar api as the MongoClient
'''
from pymongo import MongoClient

class DbClient(MongoClient):
    __doc__ = MongoClient.__doc__
    def get_collection(self,db_name , collection_name):
        '''
        :param db_name: Database name
        :param collection_name: Collection name
        :return: pymongo Collection object
        '''

        try:
            return self[db_name][collection_name]
        except KeyError , e:
            raise KeyError("This db does not have db:%s and collection:%s \n%s"%(db_name , collection_name,e))
    def insert_to_collection(self,db_name , collection_name,data):
        col = self.get_collection(db_name , collection_name)
        return col.insert(data)

if __name__ == '__main__':
    c = DbClient()
