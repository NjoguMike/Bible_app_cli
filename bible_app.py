#!/usr/bin/env python3

from models import User, Bible, Note, session
import time
from seed import bible_books, bible_version

app_user = User
note_pad = Note
bible_ref = Bible
user_logged = []

def add_bible_data():
    session.query(Bible).delete()
    session.commit()
    for b in bible_books:
        content = Bible(book = b, version = bible_version)
        session.add(content)
        session.commit()


def read_bible():
    select_book = input("Please choose a book: ")
    select_chapter = int(input("and chapter: "))
    select_verse = int(input("and verse (optional): "))
    Bible.read_book(select_book,select_chapter,select_verse)
    # return content

def user_registration():
    user = app_user(username = input("Your name please: "),
                 email = input("Email: "))
    user_logged.append(user)
    session.add(user)
    session.commit()
    print(f"Welcome ! {user.username} \n")
    
def return_user():
    user_login = input("Please enter your email to sign in: ")
    result = session.query(User).filter(User.email == user_login).first()
    user_logged.append(result)
    print(f"Welcome back ! {result.username}")

def make_notes():
    new_note = note_pad(title = str(input("Please write the title of your note: ")),
                        reference = input("What is your preferred Bible Version ? .i.e (LST, ESV, RSV, NRSV, NIV, KJV, NKJV ): "),
                        user_id = user_logged[0].id)
    session.add(new_note)
    session.commit()
    

def app():
    
    choice = 0 

    while choice != 3:
        print("\n *** Welcome to Bible App *** \n")
        print(" 1. Read ")
        print(" 2. Make Notes ")
        print(" 3. Exit \n")
        choice = int(input())
        

        if choice == 1:
            ans = input("Are you new? y/n: ")

            if ans == 'y':
                user_registration()

                Bible.books()
                read_bible()

            else:
                return_user()
                
                Bible.books()
                read_bible()


            choice = 3
            
        elif choice == 2:
            ans = input("Are you new? y/n: ")
            
            if ans == 'y':
                user_registration()

                print("Creating an account ...")
                time.sleep(3)
                make_notes()

            else:
                return_user()

                time.sleep(2)
                make_notes()

            choice = 3




if __name__ == '__main__':
    add_bible_data()
    app()


    
    
