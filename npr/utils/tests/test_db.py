import pymongo
import pymongo.collection

from ..dbmgr import DbClient
from ...settings import Settings


def test_db_client():
    c = DbClient()
    cname = "stam"
    assert isinstance(c, DbClient), "checking db client instance"
    col = c.get_collection(Settings.db.database_name, cname)
    assert isinstance(col, pymongo.collection.Collection)
    assert (col.name == cname), "collection name check"
