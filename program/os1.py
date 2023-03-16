import os  
  
try:   
    filename = 'abc.txt'  
    f = open(filename, 'r')  
    text = f.read()
    print(text)
    f.close()  
  
 
except IOError:  
    print('Problem reading: ' + filename)     
