with open ("demo.txt","r") as f:
    content = f.read()
    print(content)


with open ("demo.txt","a") as f:
    f.write("\n I am Melissa")