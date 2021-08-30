import os

import sys

import string

import random

# pip3 install cryptography

from cryptography.fernet import Fernet

# defining of function(s)

def running_of_script():

     user_prompt = input("\n> ")
     
     if user_prompt == "p": # generates password

           while True:
          
               try:
                    
                    user_inputted_length = int(input("\nEnter the no. of characters you want in your password: "))

               except ValueError:
                    
                    print("\nPlease input a numerical value.")
                    
                    continue
               
               else:
          
                    set = string.ascii_letters + string.digits + string.punctuation

                    password = ''.join([random.SystemRandom().choice(set) for _ in range(user_inputted_length)])
                    
                    passwordfile = open("password list.txt","a") # creates/acesses text file in write only mode 
                                                  
                    passwordfile.writelines(password + '\n\n')
                              
                    passwordfile.close()

                    os.system('"password list.txt"')
                    
                    running_of_script()

               break

     elif user_prompt == "k": # generates a symmetric cryptographic key
          
          while True:
          
                    try:
               
                         open("password list key.key", "r")
                    
                    except os.error:

                         key = Fernet.generate_key()

                         with open("password list key.key","wb") as filekey:

                              filekey.write(key) 
     
                         print("\nSymmetric cyptrographic key created successfully.")

                         running_of_script()
                    
                    else:

                         print("\nKey already exists!")
                         
                         running_of_script()

                    break

     elif user_prompt == "w": # wipes text file

          while True:

               try:

                    passwordfile = open("password list.txt","r")

               except os.error:

                    print("\nNo text file found, for a text file to be created you have to generate a password.")

                    running_of_script()

               else:
                    
                    passwordfile.truncate(0)
                    
                    passwordfile.close()

                    print("\nText file has been wiped...")
                    
                    running_of_script()

               break

     elif user_prompt == "o": # opens text file

          while True:

               try:

                    open("password list.txt","r")

               except os.error:

                    print("\nNo text file found, for a text file to be created you have to generate a password.")

                    running_of_script()

               else:
                    
                    os.system('"password list.txt"')
                    
                    running_of_script()

               break
     
     elif user_prompt == "c": # closes application
          
          sys.exit()

     elif user_prompt == "e": # encrypts text file with symmetric crytographic key
          
          while True:

               try:

                    # opens symmetric cryptographic key

                    with open("password list key.key","rb") as filekey:
                         
                         key = filekey.read()
                         
               except os.error:

                    print("\nNo key found to encrypt text file, generate key to encrypt text file.")

                    running_of_script()

               else:

                    # using generated key, opens text file
                    
                    fernet = Fernet(key)

                    with open("password list.txt","rb") as text_file:

                         original_text_file = text_file.read()
                         
                    # creates encrypted data

                    encrypted = fernet.encrypt(original_text_file)
                    
                    # opens text file in write olny mode and replaces original data with encrypted data

                    with open("password list.txt","wb") as encrypted_text_file:

                         encrypted_text_file.write(encrypted)

                    print("\nText file has been encrypted.")

                    running_of_script()

               break

     elif user_prompt == "d": # decrypts text file with symmetric crytographic key
          
          while True:

               try:

                    # opens symmetric cryptographic key

                    with open("password list key.key","rb") as filekey:

                         key = filekey.read()

               except os.error:

                    print("\nNo key found to decrypt text file, find and store key named:password list key.key in file path of application.")

                    running_of_script()

               else:
          
                    # using generated key, opens encrypted text file
                    
                    fernet = Fernet(key)

                    with open("password list.txt","rb") as enc_text_file:

                         encrypted = enc_text_file.read()
                    
                    # decrypting the text file

                    decrypted = fernet.decrypt(encrypted)
                    
                    # opens text file in write only mode and replaces encrypted data with decrypted data

                    with open("password list.txt","wb") as dec_text_file:

                         dec_text_file.write(decrypted)

                    print("\nText file has been decrypted.")

                    running_of_script()
               
               break

     else:
          
          print("\n[p/k] > Generate a password/symmetric cryptographic key\n\n[w/o/e/d] > Wipe/open/encrypt/decrypt text file\n\n[c] > Close application")

          running_of_script()

# excecution of function(s)/statement(s)

__location__ = os.path.realpath( # ensures any file created is created in file path of application

     os.path.join(os.path.dirname(__file__)))

print("Simple & Secure Password Generator [Version 1.0]\n\n(c) Shubham Sharma. All rights reserved.\n\nPlease read the README.md and for a list of the in-built commands use help.")

running_of_script()
