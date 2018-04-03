import unittest 
from passwordlocker import Password

class TestPassword(unittest.TestCase):

    '''
     
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    

    '''

    def setUp(self): 
            self.new_Password = Password("Collins","Kariuki","collo","karizy")
            
    def test_init(self):
    

        self.assertEqual(self.new_Password.first_name,"Collins")
        self.assertEqual(self.new_Password.last_name,"Kariuki")
        self.assertEqual(self.new_Password.username,"collo")
        self.assertEqual(self.new_Password.password,"karizy")
if __name__ == '__main__':
    unittest.main()
