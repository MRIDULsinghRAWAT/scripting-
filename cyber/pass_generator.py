# wap in python to generate a random password of length 8 containing letters, digits, and special characters.
import random
import string
def generate_pass(length=4):
    if(length<4):
        raise ValueError("length atleast 4")
    
    
