from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine =create_engine ("mysql://root:root@127.0.0.1:3306/todos")

# = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)


Base = declarative_base()

class A():
    def ash(self):
        print('you are greate ashish')
o=A()
o.ash()

