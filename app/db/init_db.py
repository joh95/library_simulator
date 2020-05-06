from app import crud
from app.core import config
from app.db.session import engine
from app.db import base
from datetime import datetime

def init_db(db_session):
    base.Book.metadata.create_all(bind=engine)

    