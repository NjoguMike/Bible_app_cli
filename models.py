from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table, func, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from seed import bible

engine = create_engine("sqlite:///bible_app.db", echo=True)
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()

bible_user = Table(
    'bible_users',
    Base.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('bible_id', ForeignKey('bibles.id')),
    extend_existing=True
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())
    email = Column(String(), unique=True ,nullable=False)

    notes = relationship('Note', back_populates='user')
    bibles = relationship('Bible', secondary=bible_user, back_populates='users')

    def __repr__(self):
        return f"User (id = {self.id}, username = {self.username}, email = {self.email})"
    
class Bible(Base):
    __tablename__ = 'bibles'

    id = Column(Integer(), primary_key=True)
    bible_chapter = Column(String())
    bible_version = Column(String())

    notes = relationship('Note', back_populates='refs')
    users = relationship('User', secondary=bible_user, back_populates='bibles')

    @classmethod
    def books(cls):
        books_list = [book["name"] for book in bible]
        print(books_list)
    
    @classmethod
    def read_book(cls, book, chapter = 0, verse = 0):
        content = [select_book["chapters"] for select_book in bible if select_book["name"] == book]
        select_chapter = [selection[(chapter - 1)] for selection in content]
        select_verse = [selection[(chapter - 1)][(verse - 1)] for selection in content]
        # print(select_verse)
        if chapter <= 0 :
            print(content)
        elif verse <= 0:
            print(select_chapter)
        else:
            print(select_verse)

    def __repr__(self):
        return f"Bible (id = {self.id}, bible_name = {self.bible_name}, bible_version = {self.bible_version})"

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    reference_chapter = Column(String())
    content = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    
    user_id = Column(Integer(), ForeignKey('users.id'))
    bible_id = Column(Integer(), ForeignKey('bibles.id'))

    # user = relationship('User', back_populates='notes')
    # refs = relationship('Bible', back_populates='notes')


    def __repr__(self):
        return f"Note (id = {self.id}, title = {self.title}, reference = {self.reference_chapter})"
    
Base.metadata.create_all(engine)