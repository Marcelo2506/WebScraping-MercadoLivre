import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../../data/data.json', lines=True)


print(df)
