
from time import sleep
import  Wikipedia_Scrape, Wikipedia_Scrape_Random

def main():     #* defining function for the main interface Window

    while True:
    
        print();print("Welcome to Wikipedia-Tool.")
        sleep(1)
        print("This program can help you fetch wikipedia articles\nYou can save them on your local machine as a word document.")
        sleep(1)
        print();print("Select an option below to continue:")
        
        print("1. Find a random Wikipedia Article")
        print("2. Fetch from a Specified Wikipedia Article")
        print("3. Exit the program");print()

        try:
            asking()

        except:
            print("Please choose between 1/2/3 only")
            asking()

def asking():     #* Selecting an option to be executed
    
    ask = int(input(">>> "))

    if ask==1:Wikipedia_Scrape_Random.main()  #* Calling the python file for a random article
    elif ask==2:Wikipedia_Scrape.main()      #* Calling the python file for user-defined article
    elif ask==3:exit()                                        #* Exiting the main program
    else:print("Invalid Choice!");main()
    
main()   #* calling the main function
