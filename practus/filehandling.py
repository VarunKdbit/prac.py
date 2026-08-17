#opening a file and read

f=open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\recursionbasics.py","r")
print(f.read())
f.close()

#file writing and creating 
#using with 
with open("par.txt","w+") as ta :
    ta.write("HI everyone\n We are learning file i/o \n using python")
    ta.seek(0)
    print(ta.read())

#file operations using with 
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","r") as t :
    print(t.read())

#append operations
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","a+") as f :
    data=f.write("\n I like to build LLM and AI agents ")
    f.seek(0)
    print(f.read())

# delete operations

import os
os.remove(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt")

#replacing particular string by another using file handling

with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\par.txt","r+") as G :
    data = G.read()
    G.write(data.replace("python","Java"))
    G.seek(0)
    print(G.read())

