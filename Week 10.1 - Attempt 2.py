import os
#The function that will be called and called again if the directory is not found
def create_file():
#get relevant information
 selecteddir = input("What directory would you like to save the file to:")
 #Check if the desired directory exists, and if not, restart the program
 if os.path.exists(selecteddir):
  print("Directory found")
 else:
  print("Directory does not exist.")
  create_file()
  #Prompt the user for the details of the file and save to variables
 filename = input("Enter the file name:")
 name = input("Enter your name:")
 address = input("Enter your address:")
 phone = input("Enter your phone number:")
 #Combine the directory with the file name string and type 
 dirComplete = os.path.join(selecteddir, filename+".txt")
 #Create a new file at the competlet directory string location
 f = open(dirComplete, "x")
 #Write the input data and close
 f.write(name + "," + address + "," + phone)
 f.close()
 #Open the file and print the contents for the user
 m = open(dirComplete, "r")
 print(m.read())
 #Exit the application
 quit()
 #Start the file writing function
create_file()
