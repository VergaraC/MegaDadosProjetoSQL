from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from secrets import credentials

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://"+credentials['username']+":"+credentials['password']+"@localhost:3306/projetosql"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL # , connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
