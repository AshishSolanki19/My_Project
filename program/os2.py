fd = "python.txt"          
file = open(fd, 'w')     
file.write("This is awesome")     
file.close()


file = open(fd, 'r')     
text = file.read()     
print(text)   
