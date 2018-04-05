#!/usr/bin/env python3.6
from passwordlocker import Password
from user_data import Userdata


def create_password(first_name, last_name, username, password):
            '''Function to create password'''
            new_password = Password(first_name, last_name, username, password)

'
