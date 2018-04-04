class Password:
    """
class that generates password and stores it
    """

    user_profile =[] #Empty profile
    def __init__(self,first_name,last_name,username,password):
        
        self.first_name =first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def save_password(self):
       
        Password.user_profile.append(self)

    def delete_password(self):
        """delete_password methods delete a saved password from user_profile"""

        Password.user_profile.remove(self)

            

        

    
