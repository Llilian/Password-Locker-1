class Userdata:

    """class accepts user input"""

    user_profile = []  # Empty profile

    def __init__(self, loginname, loginpassword):

        
        self.loginname = loginname
        self.loginpassword = loginpassword

    def save_userdata(self):

        Userdata.user_profile.append(self)

    def delete_userdata(self):
        """delete_userdata from user_profile"""

        Userdata.user_profile.remove(self)
            
