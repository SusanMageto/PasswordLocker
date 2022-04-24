class User:
  """
  Class that generates new instances of user accounts
  """
  
  user_list=[] # Empty list of users
  
  def __init__(self, username, password):
    '''
    init method that helps us define properties for our object
    Args:
    username:name of the user
    password:password of the user
    '''
    self.username= username
    self.password= password 
    
  def save_user(self):
    '''
    save_user method helps save a user to user_list
    '''
    
  