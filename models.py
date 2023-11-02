from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///bible_app.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    email = Column(String(), unique=True ,nullable=False)

    notes = relationship('Note', back_populates='user')

    def __repr__(self):
        return f"User (id = {self.id}, username = {self.username}, email = {self.email})"
    
class Bible(Base):
    __tablename__ = 'bibles'

    id = Column(Integer(), primary_key=True)
    bible_name = Column(String())
    bible_version = Column(String())

    notes = relationship('Note', back_populates='refs')

    def __repr__(self):
        return f"Bible (id = {self.id}, bible_name = {self.bible_name}, bible_version = {self.bible_version})"

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    reference = Column(String())

    user_id = Column(Integer(), ForeignKey('users.id'))
    bible_id = Column(Integer(), ForeignKey('bibles.id'))


    def __repr__(self):
        return f"Note (id = {self.id}, title = {self.title}, reference = {self.reference})"
    
Base.metadata.create_all(engine)