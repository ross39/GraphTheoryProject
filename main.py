#This will be the main method for the project.
#To run project you will need to run this file
print("Hello and welcome to the NFA Builder")
print("This was created by Ross Heaney- G00345608")

menuOpen = True
def main():
    print("===================================================================")
    menuOpen = input("Enter your regular expression as 'leave' to exit the program")
    print("===================================================================")
    regEp = input("Please enter in your regular expression")

    if(menuOpen == 'leave'  || menuOpen ='LEAVE'):
        exit()
    else:
        while menuOpen:
        print("The ifix is:", regEp)
