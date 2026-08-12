with open("par.txt","w+") as ta :
    ta.write("HI everyone\n We are learning file i/o \n using python")
    ta.seek(0)
    print(ta.read())

with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\par.txt","r+") as G :
    data = G.read()
    G.write(data.replace("python","Java"))
    G.seek(0)
    print(G.read())