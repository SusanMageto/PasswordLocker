#!/usr/bin/env python3.9
'''
This is the file that will run the application
'''
from user import User
from credentials import Credentials

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

def user_sign_in(name,password):
  '''
  function that will allow the user to sign in to their credentials account
  Args:
  name:username
  password:password used in creating user account
  '''
  sign_in=User.sign_in(name,password)
  if sign_in !=False:
    return User.sign_in(name,password)

def display_users():
  '''
  function that displays all the saved users
  '''
  return User.display_users()
  
def create_credential(userpassword,name,password):
  '''
  function to create a credential
  Args:
  userpassword:the user's password
  name:account name
  password:account password
  '''
  new_credential=Credentials(userpassword,name,password)
  return new_credential