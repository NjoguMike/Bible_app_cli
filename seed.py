from models import User, Note, session

user_1 = User(
    username = "Michael_Njogu",
    email = 'mikeynjogu@gmail.com'
)

session.add(user_1)
session.commit()