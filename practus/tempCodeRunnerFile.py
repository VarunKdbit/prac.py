
with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\par.txt","r+") as G :
    data = G.read()
    G.write(data.replace("python","Java"))
    print(G.read())