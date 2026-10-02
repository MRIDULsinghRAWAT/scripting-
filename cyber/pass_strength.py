import re
password = input("enter pass")
if(len(password)>=8 and 
re.search(r"[A-Z]",password) and 
re.search(r"[a-z]",password) and 
re.search(r"[!@#$%^&*()]",password) ):
    print("strong")
else:
    print("weak")
    
