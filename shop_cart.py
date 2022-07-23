print("Welcome to the Shopping Cart Program!\n")
print("\nPlease select one of the following: ")
print("1. Add item \n" "2. View cart \n" "3. Remove item \n" "4. Compute total \n" "5. Quit \n")

cart = []
price = []
choose = input("Please, choose a number: ")

while choose != "5":

    if choose == "1":
        item = input("Please, enter the item that you want: ")
        cart.append(item)
        item_price = float(input(f"What is the price of {item}? "))
        print(f"'{item}' has been added to the your cart.")
        price.append(item_price)
        print("\nPlease select one of the following: ")
        print("1. Add item \n" "2. View cart \n" "3. Remove item \n" "4. Compute total \n" "5. Quit \n")
        choose = input("Please, choose a number: ")
    
    elif choose == "3":
        index = int(input("Which item would you like to remove? "))
        user_remove = index - 1
        cart.pop(user_remove)
        price.pop(user_remove)
        print("Item removed.")
        print("1. Add item \n" "2. View cart \n" "3. Remove item \n" "4. Compute total \n" "5. Quit \n")
        choose = input("Please, choose a number: ")


    elif choose == "2":
        for i in range(len(cart)):
            carts = cart[i]
            prices = price[i]
            print(f"{i + 1}. {carts} - ${prices}")
        
        print("\nPlease select one of the following: ")
        print("1. Add item \n" "2. View cart \n" "3. Remove item \n" "4. Compute total \n" "5. Quit \n")
        choose = input("Please, choose a number: ")

   
   
    elif choose == "4":
        soma = sum(price)
        print(f"The total price of the items in the shopping cart is ${soma}")
        
        print("\nPlease select one of the following: ")
        print("1. Add item \n" "2. View cart \n" "3. Remove item \n" "4. Compute total \n" "5. Quit \n")
        choose = input("Please, choose a number: ")
    
    elif choose == "5":
        print("All of your products will arrive in one week, thanks for shopping with us! See you soon!")
        exit()

