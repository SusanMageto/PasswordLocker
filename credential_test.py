'''
imports unittest
imports credentials module to be tested
'''
from credentials import Credentials
import unittest

class TestingCredential(unittest.TestCase):
    '''
    Defines test cases for the Credential Class behaviours

    Args:
        unittest.TestCase : Class that helps create test cases
    '''
    
    def setUp(self):
        '''
        Method that runs before each test case
        '''

        # Create credential object
        self.new_credential = Credentials("African","Gmail","gmail20")

    def tearDown(self):
        '''
        tearDown method that cleans up after running test
        '''

        Credentials.credential_list = []
        
    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''
        self.assertEqual( self.new_credential.userpassword, "African")
        self.assertEqual( self.new_credential.credential_name, "Gmail" )
        self.assertEqual( self.new_credential.credential_password, "gmail20" )

    def test_save_credential(self):
        '''
        Test case to test if the user object is saved into the user list
        '''

        # Save the new credential
        self.new_credential.save_credential()

        self.assertEqual( len(Credentials.credential_list), 1 )
    def test_save_multiple_credentials(self):
        '''
        Test case to test if you can save multiple objects to credential list
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credentials("African2","Instagram","instagram20")

        test_credential.save_credential()

        self.assertEqual( len(Credentials.credential_list), 2)

    def test_generate_password(self):
        '''
        Test case to test if a user can log into their credentials
        '''
        
        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 9 )
        
    def test_display_credential(self):
        '''
        Test case to test if a user can see a list of all the credentials saved
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credentials("African2","Instagram","instagram20")

        test_credential.save_credential()

        test_credential = Credentials("African2","Gmail","gmail20")

        test_credential.save_credential()
        
        self.assertEqual( len(Credentials.display_credential("African2")) , 2 )
        
    def test_credential_exist(self):
        
        '''
        Test to check if we can return a boolean if we can't find the credential
        '''

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credentials("African2","Instagram","instagram20")

        test_credential.save_credential()
        
        # use contact exist method
        credential_exists = Credentials.credential_exist("Instagram")
        
        self.assertTrue(credential_exists)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)