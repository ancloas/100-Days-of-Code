#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import re
import os


# print(os.getcwd())
with open('Day 24/Input/Names/invited_names.txt', 'r') as file:
    names=file.readlines()
for name in names:
    name=name.strip('\n')
    with open('Day 24/Input/Letters/starting_letter.txt', 'r') as letter:
        content=letter.read()
    content_new= content.replace('[name]', name)
    new_path=f"Day 24/Output/ReadyToSend/file_for_{name}.text"
    file=open(new_path, 'w')
    a = file.write(content_new)
    file.close()
    print(a)

