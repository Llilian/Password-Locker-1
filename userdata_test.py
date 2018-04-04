import unittest
from passwordlocker import Password
from user_data import Userdata

class TestUserdata(unittest.TestCase):

    '''Test class'''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Userdata = Userdata("collins", "12345")
        

    def test_save_multiple_password(self):
        '''Method to check if password exists'''
        self.new_Userdata.save_userdata()
        test_userdata = Userdata("collins","12345")
        test_userdata.save_userdata()

        
        self.assertTrue(Userdata)


if __name__ == '__main__':
     unittest.main()
