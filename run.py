#!/usr/bin/env python3.9
'''
This is the file that will run the application
'''
from user import User

def create_user(name,password):
  '''
  function to create new user
  Args:
  name:the name user inputs
  password:the password the user inputs
  '''
  new_user=User(name,password)
  return new_user
  
def save_user(user):
  '''
  function that saves the user account
  Args:
  user:the user account to be saved
  '''
  user.save_user()