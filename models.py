from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///bible_app.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    email = Column(String(), unique=True ,nullable=False)

    def __repr__(self):
        username = self.username
        return username
    
class Bible(Base):
    __tablename__ = 'bibles'

    id = Column(Integer(), primary_key=True)
    bible_name = Column(String())
    bible_version = Column(String())

    def __repr__(self):
        bible = self.bible_name
        return bible

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    reference = Column(String())

    def __repr__(self):
        note = self.title
        return note