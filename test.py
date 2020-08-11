from binod.tharu import InfyHello 
from binod.tharu import hello
from binod.tharu import isBinod
from binod.tharu import SearchBinod



#binod
print("Press 1 to Print")
print("Press 2 to Print Infinitely")
print("Press 4 to Search a dir For Hidden Binod files")
choice = input()
if(int(choice) == 1):
    print(hello())
elif(int(choice) == 2):
    InfyHello()
elif (int(choice) == 4):
    SearchBinod()
