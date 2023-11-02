#!/usr/bin/env python3

from models import User, Bible, Note, session
# from seed import Interface


def app():

    # app_users = []
    app_user = User
    
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
            session.add(new_user)
            session.commit()
            choice = 3




if __name__ == '__main__':
    app()
    pass
