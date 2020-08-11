import os

def hello():
    return "binod"


def InfyHello():
    bin = True
    while bin:
        print(hello())



def isBinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():   #binod is very tricky to find, Detect all BiNoDs
        return True
    return False



def SearchBinod():
    #listing the contents of this dir
    DirContents = os.listdir()

    #for each .txt file detect
    for item in DirContents:
        if item.endswith('.txt'):
            print(f"Detecting Binod!")
            flag = isBinod(item)
            if (flag):
                print(f"Binod Found in {item}")
            else:
                print(f"Binod Not Found")