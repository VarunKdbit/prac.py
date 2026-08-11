with open("par.txt","w+") as ta :
    ta.write("HI everyone\n We are learning file i/o \n using python")
    ta.seek(0)
    print(ta.read())