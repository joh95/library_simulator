from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
CREATE TABLE book (
    id serial PRIMARY KEY,
    name varchar (50) NOT NULL,
    literary_genre varchar (50),
    author varchar (50),
    year varchar (4),
    price varchar (10));
"""