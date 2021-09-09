import os
import sys
import string
import random

# pip3 install cryptography

from cryptography.fernet import Fernet

# defining functions

def running_script():  

     user_prompt = input("\n> ")

     if user_prompt == "p": generating_password() 
     if user_prompt == "k": generating_key()
     if user_prompt == "w": wiping_text_file()
     if user_prompt == "o": opening_text_file()
     if user_prompt == "c": sys.exit() # closing application
     if user_prompt == "e": encrypting_text_file() 
     if user_prompt == "d": decrypting_text_file()
     
     else:
          
          print("\nList of in-built commands:\n\n[p/k] > Generate a password/symmetric cryptographic key\n\n[w/o/e/d] > Wipe/open/encrypt/decrypt text file\n\n[c] > Close application")
          
          running_script()

def generating_password(): 
          
     while True:

          try:

               user_inputted_length = int(input("\nEnter no. of characters for length of password: "))

          except ValueError:

               print("\nPlease input a numerical value...")
               
               continue

          else:
                         
               set = string.ascii_letters + string.digits + string.punctuation
               password = ''.join(random.SystemRandom().choice(set)
                                       
                    for _ in range(user_inputted_length))
               
               with open("password list.txt","a") as passwordfile:
                         
                    passwordfile.writelines(password + '\n\n')
                    
               print("\nPassword generated... Use 'o' to open text file.")
               
               running_script()

          break

def generating_key(): # generating symmetric cryptographic key
     
     while True:

          try: open("password list key.key", "r")

          except os.error:

               key = Fernet.generate_key()

               with open("password list key.key","wb") as filekey: filekey.write(key) 

               print("\nSymmetric cyptrographic key created...")

               running_script()

          else:

               print("\nKey already exists!")
               running_script()

          break

def wiping_text_file():
     
     while True:

          try: passwordfile = open("password list.txt","r")

          except os.error:

               print("\nText file missing... Generate password to create text file.")
               running_script()

          else:

               passwordfile.truncate(0)
               passwordfile.close()
               print("\nText file wiped...")
               running_script()

          break

def opening_text_file():

      while True:

          try: open("password list.txt","r")

          except os.error:

               print("\nText file missing... Generate password to create text file.")
               
               running_script()

          else:

               os.system('"password list.txt"')
               
               running_script()

          break

def encrypting_text_file(): # encrypting text file with symmetric crytographic key
          
     while True:

          try:

               with open("password list key.key","rb") as filekey: key = filekey.read() # opening symmetric cryptographic key; checking for already existing key

          except os.error:

               print("\nKey missing... Generate key to encrypt text file.")
               
               running_script()

          else:

               fernet = Fernet(key) # creating symmetric cryptographic key
               
               with open("password list.txt","rb") as text_file: # opening to-be-encrypted text file

                    original_text_file = text_file.read()

               encrypted = fernet.encrypt(original_text_file) # creating encrypted data

               with open("password list.txt","wb") as encrypted_text_file: # opening text file in write only mode and replacing original data with encrypted data

                    encrypted_text_file.write(encrypted)

               print("\nText file encrypted...")
               
               running_script()

          break    

def decrypting_text_file(): # decrypting text file with symmetric crytographic key
           
     while True:

          try:

               with open("password list key.key","rb") as filekey: key = filekey.read() # opening symmetric cryptographic key; checking for already existing key
                    
          except os.error:

               print("\nKey missing... Find and store key named 'password list key.key' in file path of application.")
               
               running_script()

          else:

               fernet = Fernet(key) # creating symmetric cryptographic key

               with open("password list.txt","rb") as enc_text_file: encrypted = enc_text_file.read() # opening encrypted text file using generated key

               decrypted = fernet.decrypt(encrypted) # decrypting text file

               with open("password list.txt","wb") as dec_text_file: dec_text_file.write(decrypted) # opening text file in write only mode and replacing encrypted data with decrypted data

               print("\nText file decrypted...")
               
               running_script()
               
          break

# exceuting functions and statements

__location__ = os.path.realpath( # ensuring any file created is created in file path of application

     os.path.join(os.path.dirname(__file__)))

print("Simple & Secure Password Generator [Version 1.0]\n\n(c) Shubham Sharma. All rights reserved.\n\nPlease read the README.md and use help/h for a list of the in-built commands.")

running_script()
