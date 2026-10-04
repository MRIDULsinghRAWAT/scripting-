success =0
failed=0
with open("sample.log")as file:
    for line in file:
        if "success" in line:
            success+=1
        elif "failed" in line:
            failes+=1
print ("success :", success)
print("failed:", failed)            
            