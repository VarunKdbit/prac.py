#opening a file and read

f=open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\recursionbasics.py","r")
print(f.read())
f.close()

#file operation using with 
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","r") as t :
    print(t.read())



