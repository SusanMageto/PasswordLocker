#!/usr/bin/env python3.9
'''
This is the file that will run the application
'''
from user import User

def create_user(name,password):
  '''
  function to create new user
  '''
  new_user=User(name,password)
  return new_user
  