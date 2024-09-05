def read_file():                                # This function reads our file and records its contents into the "big_list" then returns "big_list"
    menu_file = open('menu.txt', 'r')
    xxx = menu_file.readline()                   # We don't need the first line of the file

    big_list = []
    menu_contents = menu_file.readline()
    while menu_contents != "":                        # This loop records every line of the file into our list  
        menu_contents = menu_contents.rstrip("\n")
        menu_contents = menu_contents.rsplit("; ")
        big_list.append(menu_contents)                     
        menu_contents = menu_file.readline()
    
    menu_file.close()
    big_list.sort()
    return big_list


class Menu:
    
    def get_product_category(self, big_list):     # This function displays the first part of our menu: "Product Categories" and takes the first user input
        category_list = []
        for i in range (len(big_list)):
            category_list.append(big_list[i][0])     # Records every category into our category_list
        category_set = set(category_list)            # Converts our list to a set to get rid of repeating elements
        category_set = sorted(category_set)
        
        a = 1
        print("Product categories")                  
        for category in category_set:                # Prints the first part of our menu
            print(a, ". ", category, sep="")
            a += 1
        
        choice1 = input("Please select product category: ")                                                   
        while (not choice1.isdigit()) or int(choice1) > len(category_set) or int(choice1) < 1 :
            print("Error: Invalid input. Try again.")
            choice1 = input("Please select product category: ")
        print("--------------------")
        
        category_list = list(category_set)
        return choice1, category_list

    def get_product_name(self, big_list, choice1, category_list):     # This function displays the second part of our menu: "Product Names" and takes the second user input
        product_list = []                                             # It is almost identical with our first function
        choice1 = category_list[int(choice1)-1]
        for row in big_list:
            if  choice1 == row[0]:
                product_list.append(row[1])
        product_set = set(product_list)
        product_set = sorted(product_set)

        print("Products in", choice1)
        a = 1
        for product in product_set:
            print(a, ". ", product, sep="")
            a += 1

        choice2 = input("Please select product name : ")
        while (not choice2.isdigit()) or int(choice2) > len(product_set) or int(choice2) < 1 :
            print("Error: Invalid input. Try again.")
            choice2 = input("Please select product name: ")
        print("--------------------")

        product_list = list(product_set)
        return choice2, product_list

    def get_portion(self, big_list, choice2, product_list):         # This function displays the third part of our menu: "Portions" and takes the third user input
        portion_list = []                                           # It is almost identical with our first function
        choice2 = product_list[int(choice2)-1]
        for row in big_list:
            if choice2 == row[1]:
                portion_list.append(row[2])
        portion_set = set(portion_list)
        portion_set = sorted(portion_set)

        print(choice2, "Portions")
        a = 1
        for portion in portion_set:
            print(a, ". ", portion, sep="")
            a += 1

        choice3 = input("Please select product portion: ")
        while (not choice3.isdigit()) or int(choice3) > len(portion_set) or int(choice3) < 1 :
            print("Error: Invalid input. Try again.")
            choice3 = input("Please select product portion: ")

        portion_list = list(portion_set)
        return choice2, choice3, portion_list

    def get_price(self, big_list, choice2, choice3, portion_list):        # After we got our desired product, this function returns the product's price
        choice3 = portion_list[int(choice3)-1]
        for row in big_list:
            if choice2 == row[1] and choice3 == row[2]:
                price = row[3]

        return price, choice3


def main():
    big_list = read_file()
    menu = Menu()
    
    total_price = 0
    summary = ""
    keep_going = 0
    while keep_going != 2:                          # In this loop we take the first order and print two choices, if "Add New" is chosen we take another order else we terminate
        choice1, category_list = menu.get_product_category(big_list)
        choice2, product_list = menu.get_product_name(big_list, choice1, category_list)
        choice2, choice3, portion_list = menu.get_portion(big_list, choice2, product_list)
        price, choice3 = menu.get_price(big_list, choice2, choice3, portion_list)
        summary += choice2 + "   " + choice3 + "   " + price
        summary += "\n"
        price = price[1:]
        total_price += float(price)

        print("--------------------")
        print("1. Add New")
        print("2. Checkout")
        keep_going = input("Please select operation: ")
        while (not keep_going.isdigit()) or int(keep_going) > 2 or int(keep_going) < 1 :
            print("Error: Invalid input. Try again.")
            keep_going = input("Please select operation: ")
        keep_going = int(keep_going)

    print("----------------------------------------------------------------------")    
    print(summary, end="")
    print("----------------------------------------------------------------------")
    print("Total: $", format(total_price, ",.2f"), sep="")


main()