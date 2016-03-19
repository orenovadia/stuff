import pandas as pd
import numpy as np
from pymongo import MongoClient
db = MongoClient()

a = pd.DataFrame(list(db.test_database.oren.find()))
del a['_id']
print a
