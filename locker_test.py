import unittest 
from passwordlocker import Password

class TestPassword(unittest.TestCase):

    def setUp(self): 
            self.new_Password = Password("Collins","Kariuki","collo","karizy")
            
