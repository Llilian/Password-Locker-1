class Password:
    """
class that generates password and stores it
    """

    passwordlist =[] #Empty profile
    def __init__(self,first_name,last_name,username,password):
        
        self.first_name =first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def save_password(self):
       
        Password.passwordlist.append(self)

    def delete_password(self):
        """delete_password methods delete a saved password from passwordlist"""

        Password.passwordlist.remove(self)

    @classmethod            
    def find_by_username(cls, username):
            """Method taht takes in a username and returns  a password that matches that username"""
            for word in cls.passwordlist:
                if word.username == username:
                    return word

  
        
