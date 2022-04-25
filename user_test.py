'''
import unit test to create unit test for the user module
import the user module that is to be tested
'''
from user import User
from credentials import Credentials
import unittest

class TestingUsers(unittest.TestCase):
  '''
  Test class that will define the test cases for User class
  Args:
  unittest.TestCase: test class that aids in creating test cases
  '''
  
  def setUp(self):
        '''
        Set up method that runs before each test case
        '''

        # Create user object
        self.new_user = User("Unknown","African")


  def tearDown(self):
        '''
        tearDown method that clears after testing
        '''

        User.user_list = []
  def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.username, "Unknown" )
        self.assertEqual( self.new_user.userpassword, "African" )

  def test_save_user(self):
        '''
        Tests if the user object is saved into the user list
        '''

        # Saving the new user
        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )
        
  def test_save_multiple_users(self):
        '''
        Tests if you can save multiple objects to user list
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Last","Person")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)
  
  def test_find_credential(self):
        '''
        Test case to test if the User module is importing from Credential module
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Last","Person")

        test_user.save_user()

        found_credential = User.find_credential("Gmail")

        self.assertEqual( found_credential, False )
        
  def test_log_in(self):
        '''
        Tests if a user can log into their credentials
        '''

        # Save the new user
        self.new_user.save_user()

        test_user = User("Last","Person")

        test_user.save_user()

        found_credential = User.sign_in("Last", "Person")

        self.assertEqual( found_credential,  Credentials.credential_list )
        
  def test_display_user(self):
        '''
        Test case to test if a user can see a list of all the users saved
        '''
        
        self.assertEqual( User.display_user() , User.user_list )
        
  def test_user_exist(self):
        
        '''
        Tests if we can return a boolean if we can't find the user
        '''
        
        # Save the new user
        self.new_user.save_user()

        test_user = User("Last","Person")

        test_user.save_user()
        
        # use contact exist method
        user_exists = User.user_exist("Last")
        
        self.assertTrue(user_exists)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)