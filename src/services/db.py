from sqlalchemy.engine.base import Engine
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine

load_dotenv()

db_url: str = os.environ["DB_URI"]

engine: Engine = create_engine(db_url)
