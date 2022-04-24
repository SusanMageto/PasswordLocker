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
    
  