#!/usr/bin/env python3

from models import User, Bible, Note, session
# from seed import Interface
import time


def app():

    # app_users = []
    app_user = User
    note_pad = Note
    
    choice = 0 

    while choice != 3:
        print(" *** Welcome to Bible App***")
        print(" 1. Read ")
        print(" 2. Make Notes ")
        print(" 3. Exit ")
        choice = int(input())

        if choice == 1:
            ans = input("Are you new? y/n :")
            new_user = app_user(username = input("Your name please : "),
                 email = input("Email : ")) if ans == "y" else print("signing you in ...")
            print(new_user)
            if ans == 'y':
                session.add(new_user)
                session.commit()
            choice = 3
            
        elif choice == 2:
            ans = input("Are you new? y/n :")
            new_user = app_user(username = input("Your name please : "),
                 email = input("Email : ")) if ans == "y" else print("signing you in ...")
            if ans == 'y':
                session.add(new_user)
                session.commit()
                print("Creating an account ...")
                time.sleep(5)
                new_note = note_pad(title = str(input("Please write the title of your note :")),
                                     reference = input("What is your preferred Bible Version ? .i.e (LST, ESV, RSV, NRSV, NIV, KJV, NKJV )"))
                                     
            else:
                time.sleep(3)
                new_note = note_pad(title = str(input("Please write the title of your note :")),
                                     reference = input("What is your preferred Bible Version ? .i.e (LST, ESV, RSV, NRSV, NIV, KJV, NKJV )"))
                # print(new_note)
                session.add(new_note)
                session.commit()
            choice = 3




if __name__ == '__main__':
    app()
    pass
