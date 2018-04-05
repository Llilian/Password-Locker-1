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



