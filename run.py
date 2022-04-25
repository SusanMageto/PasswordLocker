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

def save_credential(credential):
  '''
  function that allows us to save credentials
  '''
  credential.save_credential()
  
def check_existing_credential(name):
  '''
  function that checks if the credential name already exists
  Args:
  name:credential name
  '''
  return Credentials.credential_exist(name)

def display_credentials(password):
  '''
  function that displays all saved credentials with their passwords
  '''
  return Credentials.display_credentials(password)

def create_generated_password (name):
  '''
  function that will generate a passowrd for the user
  Args:
  name:account name
  '''
  password=Credentials.generate_password()
  return password

def main():
  '''
  function for running this app
  '''
  print ('''Hello! Welcome to password Locker \n Use the following codes to navigate the app''')
  
  while True: 
    '''
    loop to run the whole app
    '''
    print ('''
           short codes:
           ca - create password locker account \n
           dn - display names of current password locker users
           si - sign into your password locker account
           ex - exit password locker account
           '''
    
    #to get short code from user
    short_code=input().lower()
    
    if short_code=='ca'
          '''
          create password locker account
          '''
         print("\n")
            print("New Password Locker Account")
            print("-"*10)

            print("User name ...")
            username = input()

            print("Password ...")
            userpassword = input()

            # Create and save new user
            save_users( create_user( username, userpassword) )

            print("\n")
            print(f"{username} welcome to Password Locker")
            print("\n")
    )



if __name__ == '__main__':

    main()