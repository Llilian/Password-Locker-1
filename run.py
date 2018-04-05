#!/usr/bin/env python3.6
from passwordlocker import Password
from user_data import Userdata


def create_password(first_name, last_name, username, password):
            '''Function to create password'''
            new_password = Password(first_name, last_name, username, password)

def save_password(Password):
            '''Function to save password'''
            Password.save_password

def del_password(password):
            '''fuunction to delete password'''
            password.delete_password()

def find_password(username):
            '''function to find password'''
            return Password.find_by_username(username)

def check_existing_password(username):
            '''function to check if password exists and return boolean '''
            return Password.passwordlist(username)
    
def display_contacts():
            '''Function to display all saved passwords'''
            return Userdata.display_passwords()



def main():
    print("Hello Welcome to Password list. What is your name?")
    username = input()

    print("Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use this short codes : pp - create a new password dp - delete password, fp -find password, ep -exit password list")

        short_code = input ().lower()

        if short_code == "pp":
            print("++++++ New Password....++++++")
            print("-"*10)

            print ("++++++ First name....+++++++")
            first_name = input()

            print ("++++++ Last Name......+++++++")
            last_name = input()

            print ("++++++ Username ........+++++++")
            username = input()

            print ("#####Password.........########")
            password = input()


            save_password(create_password(first_name,last_name,username,password)) #create and save new password
            print ('\n')
            print ("Userdata {first_name}{last_name} created")
            print ('\n')
        

        elif short_code == 'dp':
            
            if display_password():
                print("##### Here i$ A L!st of all Passwords #####")
                print('\n')

                for password in display_password():
                    print("{password.first_name} {password.last_name}.....{password.username}")

                    print('\n')
            
            else:
                    print('\n')
                    print("You dont seem  to have an  #### Password #### saved yet")
                    print('\n')

        elif short_code == 'fp':

                print("Enter the + Username + u wana search for")

                search_username = input()
                if check_existing_password(search_username):
                    search_password = find_password(search_username)
                    print("{search_password.first_name} {search_password.last_name}")
                    print ('-'*20)

                    print("Username ......{search_password.username}")
                    print("Password ......{search_password.password}")

                else:

                    print("That Password does not exist")

        elif short_code == "ex":
                print("Bye ....")
                break
        else:
            
                print("I really dint get that Please use the short codes")


if __name__ == '__main__':

    main()
