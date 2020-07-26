'''
Created on 20 Jul 2020

@author: Marty
'''
# Python program to illustrate 
# Append vs write mode 
file1 = open("myfile.txt","w") 
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
file1.close() 
  
# Append-adds at last 
file1 = open("myfile.txt","a")#append mode 
file1.write("Today \n") 
file1.close() 
  
file1 = open("myfile.txt","r") 
print("Output of Readlines after appending")
print( file1.readlines()) 
print()
file1.close() 
  
# Write-Overwrites 
file1 = open("myfile.txt","w")#write mode 
file1.write("This is Delhi \nThis is Paris \nThis is London \n") 
file1.close() 
  
file1 = open("myfile.txt","r") 
print ("Output of Readlines after writing")
print (file1.readlines() )
print()
file1.close() 