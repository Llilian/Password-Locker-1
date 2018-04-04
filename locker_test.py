import unittest 
from passwordlocker import Password

class TestPassword(unittest.TestCase):

    def setUp(self): 
        '''
        Set up method to run before each test cases.
        '''
        self.new_Password = Password("Collins","Kariuki","collo","karizy")

    def tearDown(self):
        """ clearing the array """
        Password.user_profile = []

    def test_init(self):
    
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Password.first_name,"Collins")
        self.assertEqual(self.new_Password.last_name,"Kariuki")
        self.assertEqual(self.new_Password.username,"collo")
        self.assertEqual(self.new_Password.password,"karizy")



    def test_save_Password(self):

        self.new_Password.save_password()
        self.assertEqual(len(Password.user_profile),1)



 #class creation
    
    def test_save_multiple_password(self):
        '''test_save_multiple_password to check if we can save multiple passwords'''
        self.new_Password.save_password()
        test_password = Password("Test","user","collo","test@user.com")
        test_password.save_password()
        self.assertEqual(len(Password.user_profile),2)

    def test_delete_password(self):
        """test_delete_password to test if we can remove list"""
        #self.new_Password.save_password()
        test_password =Password("Test","user","collo","test@user.com")
        test_password.save_password()
        test_password.delete_password()
        
        self.assertEqual(len(Password.user_profile),0)

    def test_find_password_by_username(self):
        """test to see if we can find pass word"""

        #self.new_Password.save_password()
        test_password = Password("Test","user","collo","test@user.com")
        test_password.save_password()

        found_Password =Password.find_by_username("collo")
        self.assertEqual(found_Password.password,test_password.password)

    
if __name__ == '__main__':
     unittest.main()
 

 
