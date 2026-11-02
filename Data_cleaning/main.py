import pandas as pd
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(override=True)

engine = create_engine(os.getenv("DATABASE_URL"))

df = pd.read_sql("SELECT * FROM urbanpiper_raw_sales", engine)

print(df.columns)