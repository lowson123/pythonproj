import pymongo
mongo = pymongo.MongoClient(host="localhost",port=27017)
db = mongo["ChampsSports"]
collection = db["Shoes"]

def menu():
     print("[1] Update Inventory")
     print("[2] Add Inventory")
     print("[3] Display Inventory")
     print("[4] Delete Inventory")
     print("[0] Exit the program")

option = 8

while option != 0:
    menu()
    option = int(input("Enter your option: "))

    if option == 1:
        #do option 1 stuff
        print("You're now updating the inventory")
        updinv = input("Please type shoe brand:\t")
        vnidda = { "Shoe_Brand": updinv}
        updvni = input("Enter Updated Quantity:\t")
        newvalues = { "$set": {"Quantity":updvni}}
        collection.update_one(vnidda, newvalues)
        print("Inventory is now updated\n")
        continue
    elif option == 2:
        #do option 2 stuff
        print("You're now adding to inventory")
        addbrand = input("Please type new shoe brand:\t")
        addquantity = input("Enter Quantity:\t")
        mydict = {"Shoe_Brand": addbrand, "Quantity": addquantity}
        collection.insert_one(mydict)
        print("New Shoe brand added")
        continue


    elif option == 3:
        #do option 3 stuff
        print("Current Inventory")
        for x in collection.find():
            print(x)
        continue

    elif option == 4:
        #do option 4 stuff
        deleteshoe = input("Which shoe would you like to delete?\t")
        remshoe = {"Shoe_Brand": deleteshoe}
        collection.delete_one(remshoe)
        print("Shoe has been removed")
        continue

    elif option == 0:
        break
    else:
        print("Invalid option please choose numbers provided below")
        continue


print("Thanks for using this program.  Goodbye.")