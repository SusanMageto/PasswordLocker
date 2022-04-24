class User:
  """
  Class that generates new instances of user accounts
  """
  
  user_list=[] # Empty list of users
  
  def __init__(self, user_name, password):
    '''
    init method that helps us define properties for our object
    Args:
    user_name:name of the user
    user_password:password of the user
    '''
    self.user_name= user_name
    self.user_password= password 
  