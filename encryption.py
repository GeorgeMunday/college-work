key = 42  
data = open("encryption.txt", "rb").read()  
open("encryption.txt", "wb").write(bytes([b ^ key for b in data])) 


