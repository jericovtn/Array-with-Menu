# Name: Jerico James F. Viteño
# Laboratory Exercise 1: Array Menu
# November 5, 2022

# Array
list = [22, 33, 55, 44, 66, 77, 11, 99, 88, 111]

# Menu
def array():
    print("\n" + "—" * 42)
    print((" " * 19 + "ARRAY"))
    print("—" * 42)
    print(list, '\n')

def menu():
    print("—" * 42)
    print(" "*19 + "MENU")
    print("—" * 42)
    print("\t 1.   Add an element")
    print("\t 2.   Insert an element")
    print("\t 3.   Modify an element")
    print("\t 4.   Delete an element")
    print("\t 5.   Arrange in ascending order")
    print("\t 6.   Arrange in descending order\n")

for i in range(0,9):

    # Display: Array and Menu
    array()
    menu()

    # Input: Option in the Menu
    print(" " * 19, "•••")
    option = int(input("\t\tWhat would you like to do? "))

    # 1. Add an element
    if option == 1:
        print("\n" + "—" * 42)
        print(" "*13 + "ADD AN ELEMENT")
        print("—" * 42)
        list.append(int(input("Enter an element: ")))
        print(" " * 19, "•••")
        print("\t\tNew element has been added")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    # 2. Insert an element
    elif option == 2:
        print("\n" + "—" * 42)
        print(" "*13 + "INSERT AN ELEMENT")
        print("—" * 42)
        print("(ex. 2; before the third value)")
        insertIndex = int(input("Enter the number of index: "))
        insertValue = int(input("Enter the value: "))
        list.insert(insertIndex, insertValue)
        print(" " * 19, "•••")
        print("\t\tNew element has been inserted")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    # 3. Modify an element
    elif option == 3:
        print("\n" + "—" * 42)
        print(" "*13 + "MODIFY AN ELEMENT")
        print("—" * 42)
        print("(ex. 2; the place of the value you want to replace)")
        modifyIndex = int(input("Enter the number of index: "))
        modifyValue = int(input("Enter the value:"))
        list[modifyIndex] = modifyValue
        print(" " * 19, "•••")
        print("\t\tNew element has been modified")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    # 4. Delete an element
    elif option == 4:
        print("\n" + "—" * 42)
        print(" "*13 + "DELETE AN ELEMENT")
        print("—" * 42)
        list.remove(int(input("Enter an element: ")))
        print(" " * 19, "•••")
        print("\t\tAn element has been deleted")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    # 5. Arrange in ascending order
    elif option == 5:
        print("\n" + "—" * 42)
        print(" "*8 + "ARRANGE IN ASCENDING ORDER")
        print("—" * 42)
        list.sort()
        print(" " * 19, "•••")
        print("Elements has been arranged in ascending order")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    # 6. Arrange in descending order
    elif option == 6:
        print("\n" + "—" * 42)
        print(" "*8 + "ARRANGE IN DESCENDING ORDER")
        print("—" * 42)
        list.sort()
        list.reverse()
        print(" " * 19, "•••")
        print("Elements has been arranged in descending order")
        print("—" * 42)
        print(" " * 16 + "NEW ARRAY")
        print("—" * 42 + "\n", list)
        print(" " * 19, "•••\n")

    else:
        print("\n   I'm sorry, this is not a valid option!")
        print(" " * 19, "•••")


    tryAgain = input("\nDo you want to use Address Book again? \n(yes/no): ")
    if tryAgain == "Yes" or tryAgain == "yes" or tryAgain == "YES":
        continue
    elif tryAgain == "Y" or tryAgain == "y":
        continue
    else:
        print("\n\nThank you, have a nice day!  \nAddress Book is Closed.")
        break






