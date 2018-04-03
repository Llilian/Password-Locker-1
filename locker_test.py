import unittest 
from passwordlocker import Password

class TestPassword(unittest.TestCase):

    def setUp(self): 
            self.new_Password = Password("Collins","Kariuki","collo","karizy")
            
    def test_init(self):
    

        self.assertEqual(self.new_Password.first_name,"faith")
        self.assertEqual(self.new_Password.last_name,"thuita")
        self.assertEqual(self.new_Password.username,"fait")
        self.assertEqual(self.new_Password.password,"faiy")
