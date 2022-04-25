from credentials import Credentials
from run import display_users


class User:
  """
  Class that generates new instances of user accounts
  """
  
  user_list=[] # Empty list of users
  
  def __init__(self, username, userpassword):
    '''
    init method that helps us define properties for our object
    Args:
    username:name of the user
    password:password of the user
    '''
    self.username= username
    self.userpassword= userpassword 
    
  def save_user(self):
    '''
    save_user method helps save a user to user_list
    '''
    User.user_list.append(self)
    
@classmethod
def find_credentials(cls,name):
  '''
  a class method used to check if there is correct importation of the credentials
  Args:
  name:credential name
  '''
  for credential in Credentials.credential_list:
    if credential.credential_name==name:
      return True
    return False
@classmethod
def sign_in(cls, name, password):
  '''
  a class method that allows the user to sign in
  Args:
  name:username
  password:userpassword
  '''
  # Search for the user in the user list
  for user in cls.user_list:
    if user.username == name and user.userpassword == password:
      return Credentials.credential_list
    return False
  
@classmethod 
def display_users(cls):
  '''
  a class method that returns the list of users
  '''
  return cls.user_list

@classmethod
def user_exist(cls,name):
  '''
  method to check if a user exists in the list of users.
  '''
  for user in cls.user_list:
    if user.username == name:
      return True
    return False
  
            
                
            
       

  
  