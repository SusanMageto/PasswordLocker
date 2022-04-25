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
           dn - display names of current password locker users \n
           si - sign into your password locker account \n
           ex - exit password locker account
           ''')
    
    #to get short code from user
    short_code=input().lower()
    
    if short_code=='ca':
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
          save_user( create_user( username, userpassword) )

          print("\n")
          print(f"{username} welcome to Password Locker")
          print("\n")
    
    elif short_code == 'dn':
            '''
            Display the names of the current users 
            '''
            if display_users():
              print("\n")
              print("Here is the list of the current users of Password Locker")
              print("-"*10)

              for user in display_users():
                    print(f"{user.username}")
                    print("-"*10)
            else:
                print("\n")
                print("There are no current users in Password Locker. \n    Be the first user :)")
                print("\n")
                
    elif short_code == 'si':
            '''
            Signs the user into their Password Locker account
            '''
            print("\n")
            print("Sign into Password Locker Account")
            print("Enter the user name")
            username = input()

            print("Enter the password")
            userpassword = input()

            if user_sign_in(username,userpassword) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                user_sign_in(username,userpassword)
                print("\n")
                print(f'''{username} welcome to your Credentials\n
                Use these short codes to navigate''')
                
                while True:
                    '''
                    Loop to run functions after signing in
                    '''
                    print('''  Short codes:
        cc - add a credential \n
        dc - display credentials \n
        cp - create a credential with a generate password \n
        ex - exit Credentials''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a Credential
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credential(create_credential( userpassword, credential_name, credential_password) )

                        print("\n")
                        print(f"Credentials for {credential_name} have been created and saved")
                        print("\n")
                    elif short_code == 'dc':
                        '''
                        Displays credential name and password
                        '''

                        if display_credentials(userpassword):
                            print("\n")
                            print(f"{username}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(userpassword):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")
                            
                    elif short_code == 'cp':
                        '''
                        Creating a credential with a generated password
                        '''

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        # Saves new credential with its generated password
                        save_credential( Credentials(userpassword, credential_name, (create_generated_password(credential_name)) ) )
                        print("\n")
                        print(f"Credentials for {credential_name} have been created")
                        print("\n")
                        
                    elif short_code == 'ex':
                        print(f"See you later {username}")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f'''{short_code} does not compute.
    Please use the short codes provided''')
                        print("\n")  
                        
                        
    elif short_code == 'ex':
            '''
            Exit Password Locker
            '''
            print("\n")
            print("Bye .....")

            break

    else:
            print("\n")
            print(f'''Come again, what's {short_code}?
    Please use the short codes''')
            print("\n")

                
if __name__ == '__main__':

    main()