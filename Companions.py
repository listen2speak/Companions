import sys
import time
import json
import os.path
from os import path

# set both lists
friends = []
pets = []

#define Write to JSON file method and read methods for both lists

def writeToJSONFile(path,fileName,data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data,fp)

#opens JSON file and appends each item to required list
def readFriendsJSONFile():
    if path.exists("friends.json") == True:
        with open('friends.json') as f:
            friends_data = json.load(f)
            x = 0
            while x < len(friends_data):
                friends.append(friends_data[x])
                x = x + 1
    else:
        return

def readPetsJSONFile():
    if path.exists("pets.json") == True:
        with open('pets.json') as p:
            pets_data = json.load(p)
            x = 0
            while x < len(pets_data):
                pets.append(pets_data[x])
                x = x + 1
    else:
        return

#sets options to call functions

def friendsList(option):
    
    while option !=0:
        if option == 1:
            add_friends()
            return 
        elif option == 2:
            add_pets()
            return
        elif option == 3:
            list_friends()
            return

        elif option == 4:
            list_pets()
            return

        elif option == 5:
            del_friends()
            return

        elif option == 6:
            del_pets()
            return

        elif option == 7:
            petsJSON()
            friendsJSON()
            print("Data saved!")
            return
        
        elif option >=8:
            print("Not a valid option. Try again!")
            option = int(input(menu))

        elif option < 0:
            print("Not a valid option. Try again!")
            option = int(input(menu))

    return 
    
    
    
#functions

#add friends 
def add_friends():
    while True:
        friends_temp = input("\nPlease enter a friend's name or press '0' to return to menu:\n")
        if friends_temp != '0':
            friends.append(friends_temp)    
        else:
            return 

#add pets 
def add_pets():
    while True:
        pets_temp = input("\nPlease enter a pet's name or press '0' to return to menu:\n")
        if pets_temp != '0':
            pets.append(pets_temp)    
        else:
            return 

#list friends 
def list_friends():
    friends.sort()
    print("\n*** Friends List ***\n")
    x = 0
    while x < len(friends):
        print(friends[x])
        x = x + 1
    print("\n*** End of List ***\n")
    return

# defines variables and calls method to write Friends list to JSON file
def friendsJSON():
    path = './'
    fileName = 'Friends'
    data = friends
    writeToJSONFile(path, fileName, data)
    return

#list pets
def list_pets():
    pets.sort()
    print("\n*** Pets List ***\n")
    x = 0
    while x < len(pets):
        print(pets[x])
        x = x + 1
    print("\n*** End of List ***\n")
    return

#defines variables and calls method to write Pets lists to JSON file
def petsJSON():
    path = './'
    fileName = 'Pets'
    data = pets
    writeToJSONFile(path, fileName, data)
    return

#sets delete options to friends list
def del_friends():
    while True:

        # if no friends, return to menu
        if len(friends) == 0:
            print ("No friends in list to delete. \nReturning to menu.")
            return

        # input name of friend to remove
        remove_friend = input("\nType a friend to remove or press '0' to return to menu.\n")

        # calls binary search method to locate name, if found, removes from list and verifies more items in list
        if remove_friend != '0':
            if search(friends, remove_friend) == True:
            
                friends.remove(remove_friend)
                print(remove_friend + " has been removed from the list.\n")

                if 0 == len(friends):
                    print ("No more friends listed. \nReturning to menu.")
                    return
                
            else:
                print(remove_friend + " is not listed.\nTry again.\n")
        else:
            return
       
#sets delete options to pets list same as del_friends
def del_pets():
    while True:
        if len(pets) == 0:
            print ("No pets in list to delete. \nReturning to menu.")
            return
        
        remove_pet = input("\nType a pet to remove or press '0' to return to menu.\n")
        
        if remove_pet != '0':
                        
            if search(pets, remove_pet) == True:
                pets.remove(remove_pet)
                print(remove_pet + " has been removed from the list.\n")

                if len(pets) == 0:
                    print ("No more pets listed. \nReturning to menu.")
                    return
                
            else:
                print(remove_pet + " is not listed.\n Try again.\n")
        else:
            return

#search list via Binary Search    
def search(list_type, name):

    #sorts list
    list_type.sort()

    #sets low and high variables
    low = 0
    high = len(list_type)-1

    #finds mid point in the sorted list
    while low <= high:
        mid = (low + high) // 2
        if name == list_type[mid]:
            return True
        elif name < list_type[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


###main###

#sets variable for name input and menu items
name = input("What is your name? ")
menu = "\n1 = Add Friends \n2 = Add Pets \n3 = Print Friends \n4 = Print Pets \n5 = Delete Friends\n6 = Delete Pets\n7 = Save to JSON\n0 = exit\nChoose an option:\n "

print ("\nHello " + name + "!\n")

#exception incase of input to main menu failure.    
try:
    readFriendsJSONFile()
    readPetsJSONFile()
    option = 1
    while option != 0:
        option = int(input(menu))
        friendsList(option)

except ValueError:
    print("Please use integers in the menu.\nSaving data and exiting.\n")
    petsJSON()
    friendsJSON()
    sys.exit

#when exiting program saves list to both friends and pets JSON files and countsdown to sys.exit
print ("\nGood bye " + name)
petsJSON()
friendsJSON()
print("Exiting in\n3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
sys.exit


    
            

