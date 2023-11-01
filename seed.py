from models import User, Note, session, Bible

session.query(User).delete()
session.query(Bible).delete()
session.query(Note).delete()

user_1 = User(
    username = "Michael_Njogu",
    email = 'mikeynjogu@gmail.com'
)

session.add(user_1)
session.commit()

bible = Bible(
    bible_name = "The Harper Collins Bible",
    bible_version = 'New Revised Standard Version'
)

note = Note(
    title = "Alive in Christ",
    reference = 'Ephesians'
)

session.bulk_save_objects([bible,note])
session.commit()