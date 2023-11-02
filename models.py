from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from seed import bible

engine = create_engine("sqlite:///bible_app.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    email = Column(String(), unique=True ,nullable=False)

    notes = relationship('Note', backref='user')

    def __repr__(self):
        return f"User (id = {self.id}, username = {self.username}, email = {self.email})"
    
class Bible(Base):
    __tablename__ = 'bibles'

    id = Column(Integer(), primary_key=True)
    bible_chapter = Column(String())
    bible_version = Column(String())

    notes = relationship('Note', backref='refs')

    @classmethod
    def chapters(cls):
        chapter_list = [book["name"] for book in bible]
        print(chapter_list)
    
    @classmethod
    def read_book(cls, book, chapter = 1, verse = 1):
        content = [select_book["chapters"] for select_book in bible if select_book["name"] == book]
        select_chapter = [selection[(chapter - 1)] for selection in content]
        select_verse = [selection[(chapter - 1)][(verse - 1)] for selection in content]
        # print(select_verse)
        if chapter > 1 :
            print(select_chapter)
        elif chapter > 1 and verse > 1 :
            print(select_verse)
        else:
            print(select_chapter)

    def __repr__(self):
        return f"Bible (id = {self.id}, bible_name = {self.bible_name}, bible_version = {self.bible_version})"

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    reference_chapter = Column(String())
    content = Column(String())

    user_id = Column(Integer(), ForeignKey('users.id'))
    bible_id = Column(Integer(), ForeignKey('bibles.id'))


    def __repr__(self):
        return f"Note (id = {self.id}, title = {self.title}, reference = {self.reference_chapter})"
    
Base.metadata.create_all(engine)