#opening a file and read

f=open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\recursionbasics.py","r")
print(f.read())
f.close()

#file operation using with 
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","r") as t :
    print(t.read())

#append operation
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","a+") as f :
    data=f.write("\n I like to build LLM and AI agents ")
    f.seek(0)
    print(f.read())

