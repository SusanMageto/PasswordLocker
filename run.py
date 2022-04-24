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
  return user.save_user()
  
def check_existing_users(name):
  '''
  function that checks if the username already exists
  Args:
  name:the username
  '''
  return User.user_exist(name)
  
  