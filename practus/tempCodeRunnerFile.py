with open(r"C:\Users\Varun\OneDrive\Desktop\pracpro\practus\demo.txt","a+") as f :
    data=f.write("\n I like to build LLM and AI agents ")
    f.seek(0)
    print(f.read())
