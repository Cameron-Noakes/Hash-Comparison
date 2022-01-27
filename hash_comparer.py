
# Hash comparison project ##################

# This project is to compare messages, often you can have many messages that look the same but are not.
# This program solves this issue, since if 1 letter is different it will create an entirely different hash
# this is a good way to determine quickly if two messages are the same.
# License: Cameron Noakes


import hashlib

# User Inputs
def inputs():

    global message1
    global message2
    message1 = input("Enter a message to hash and compare: ")
    message2 = input("Enter the second message to hash and compare: ")
    hashing()


# Calculating the Hashes - with the encoding needed.
def hashing():
    global hash1
    global hash2
    hash1 = hashlib.md5(message1.encode("utf-8")).hexdigest()
    hash2 = hashlib.md5(message2.encode("utf-8")).hexdigest()
    outputs()

#Outputs
def outputs():
    
    # Print out inputs
    print ("The Inputs given: \n")
    print (message1, end="\n")
    print (message2, "\n")
    
    # Print out hashes of the inputs.
    print ("The output hashes: \n", end="")
    print (hash1)
    print (hash2)
    comparision()

def comparision():
    
    if hash1 == hash2:
        print ("Both Hashes match and are the same!")
        endif
    
    else:
        print ("the hashes are not the same.")


inputs()