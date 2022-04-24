'''
credential module by Sue
Imports the random module from python for password generation
imports the string module from python for password generation
imports the user from the user module so as to get access to the user
'''
from random import choice
import string
from user import User

class Credentials:
  
 """
Class that generates new instances of credentials for the users
"""

credentials_list=[] #Empty list of credentials

def __init__(self,userpassword,credential_name,credential_password):
  '''
  init method that helps us define properties for our user object
  Args:
  password:the user's password
  credential_name:name of the credential account
  credential password:password for the credential account
  '''
  self.userpassword=userpassword
  self.credential_name=credential_name
  self.credential_password=credential_password
  
def save_credentials(self):
  '''
  a method that saves credentials to credentials list
  '''
  Credentials.credentials_list.append(self)