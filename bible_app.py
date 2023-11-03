#!/usr/bin/env python3

from models import User, Bible, Note, session
# from seed import Interface
import time
# from seed import bible


def app():

    # app_users = []
    app_user = User
    note_pad = Note
    
    choice = 0 
        

    while choice != 3:
        print("\n *** Welcome to Bible App *** \n")
        print(" 1. Read ")
        print(" 2. Make Notes ")
        print(" 3. Exit \n")
        choice = int(input())
        

        if choice == 1:
            ans = input("Are you new? y/n: ")
            user = app_user(username = input("Your name please: "),
                 email = input("Email: ")) if ans == "y" else input("Please enter your email to sign in: ")

            if ans == 'y':
                session.add(user)
                session.commit()

                print(f"Welcome ! {user.username}")
                Bible.books()
                select_book = input("Please choose a book: ")
                select_chapter = int(input("and chapter: "))
                Bible.read_book(select_book,select_chapter)

            else:
                result = session.query(User).filter(User.email == user).first()
                print(f"Welcome back ! {result.username}")
                Bible.books()
                select_book = input("Please choose a book: ")
                select_chapter = int(input("and chapter: "))
                Bible.read_book(select_book,select_chapter)
                # content = 

            choice = 3
            
        elif choice == 2:
            ans = input("Are you new? y/n: ")
            user = app_user(username = input("Your name please: "),
                 email = input("Email: ")) if ans == "y" else input("Please enter your email to sign in: ")
            if ans == 'y':
                session.add(user)
                session.commit()
                print("Creating an account ...")
                time.sleep(3)
                new_note = note_pad(title = str(input("Please write the title of your note: ")),
                                     reference = input("What is your preferred Bible Version ? .i.e (LST, ESV, RSV, NRSV, NIV, KJV, NKJV ): "),
                                     user_id = user.id)
                session.add(new_note)
                session.commit()
                                     
            else:
                result = session.query(User).filter(User.email == user).first()
                print(f"Welcome back ! {result.username}")

                time.sleep(3)
                new_note = note_pad(title = str(input("Please write the title of your note : ")),
                                     reference = input("What is your preferred Bible Version ? .i.e (LST, ESV, RSV, NRSV, NIV, KJV, NKJV )"),
                                     user_id = result.id)
                # print(new_note)
                session.add(new_note)
                session.commit()
            choice = 3




if __name__ == '__main__':
    app()
    # Bible.read_book("Genesis",2,2)
    
