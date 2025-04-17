itemlist = []
pricelist = []

def additem(item, price):
    itemlist.append(item)
    pricelist.append(price)
    print("Item has been added to your cart.")

def removeitem():
    itemre = input("Enter the item you want to remove: ")
    if itemre in itemlist:
        index = itemlist.index(itemre)
        itemlist.pop(index)
        pricelist.pop(index)
        print(f"{itemre} has been removed from your cart.")
    else:
        print("Item not found in cart.")

def viewcart():
    if not itemlist:
        print("Your cart is empty.")
    else:
        print("Your shopping cart:")
        for i in range(len(itemlist)):
            print(f"{itemlist[i]} - ${pricelist[i]}")

while True:
    print("------ Market Menu ------")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        item = input("Enter the item you want to add: ")
        try:
            price = float(input("Enter the price of the item: "))  # Convert price to float
            additem(item, price)
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")
    elif choice == 2:
        removeitem()
    elif choice == 3:
        viewcart()
    else:
        print("Invalid choice, please try again.")
