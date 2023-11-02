from models import User, Note, session, Bible

# session.query(User).delete()
# session.query(Bible).delete()
# session.query(Note).delete()

# user_1 = User(
#     username = "Michael_Njogu",
#     email = 'mikeynjogu@gmail.com'
# )

# session.add(user_1)
# session.commit()

# bible = Bible(
#     bible_name = "The Harper Collins Bible",
#     bible_version = 'New Revised Standard Version'
# )

# session.add(bible)
# session.commit()

# user = session.query(User).filter([person.id for person in User.username])
# print()

# note = Note(
#     title = "Alive in Christ",
#     reference = 'Ephesians',
#     user_id = user.id
# )

# session.add(note)
# session.commit()