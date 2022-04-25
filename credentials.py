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
  
@classmethod
def generate_password(cls):
  '''
  a class method that generate an alphanumeric password
  '''
  #gives us the number of characters in our password
  size=9
  
  #generate a random alphanumeric password
  alphanumeric=string.ascii_lowercase+string.digits+string.ascii_uppercase
  
  #creates password
  password=''.join( choice(alphanumeric) for num in range(size))
  return password

@classmethod
def display_credentials(cls,password):
  '''
  a class method that returns the credential list
  '''
  users_credentials_list=[]
  for credential in cls.credentials_list:
    if credential.userpassword==password:
      users_credentials_list.append(credential)
      return users_credentials_list
    
@classmethod
def credential_exist(cls,name):
  '''
  a class method that checks if a credential exists in the list of credentials
  Args:
  name: credential name
  will return a boolean value:true/false
  '''
  for credential in cls.credential_list:
    if credential.credential_name==name:
      return True
    return False
  