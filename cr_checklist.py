# Create our Checklist
print()
checklist = list()

# Define Functions
#Create function is going to add the input of item and append it to the checklist
def create(item):
  checklist.append(item)

# Read function will return the value that lives at that index in our checklist and save it in item
def read(index):
    item = checklist[index]
    return item

#Update function is overwriting the data located in the second position of the list
def update(index, item):
    checklist[index] = item

#Destroy function is going to remove designated input value of index
def destroy(index):
    checklist.pop(index)

# For loop will iterate (perform repeatedly)over all items in checklist and pass each value into code block below it as the value listitem
#
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def user_input(prompt):
    user_input = input(prompt).lower().upper()
    return user_input

def select(function_code):
    #ADD ITEM
    if function_code == "A":
        input_item = user_input("Input item to add: ")
        create(input_item)
    
    #READ ITEM
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))
        read(item_index)

    #UPDATE ITEM
    elif function_code == "U":
        item_index = int(user_input("Which index to update? "))
        input_item = (user_input("Input update: "))
        update(item_index, input_item)
        


    #DESTROY ITEM
    elif function_code == "D":
        item_index = int(user_input("Which index would you like to delete: "))
        destroy(item_index)
  
    #DISPLAY ALL ITEMS
    elif function_code == "P":
        list_all_items()
    
    #QUIT PROGRAM
    elif function_code == "Q":
         return False

    # #UNKKNOWN OPTION    
    else:
        print("Unknown Option")
    return True






# #TEST
def test():

    create("RED SHIRT")
    create("ORANGE PANTS")
    create("YELLOW SOCK")
    create("GREEN SOCK")
    create("BLUE SHOE")
    create("INDIGO SHOE")
    create("VIOLET UNDERWEAR")
    

#     print(read(0))
#     print(read(1))

#     update(0, "purple socks")
#     destroy(1)

#     print(read(0))
#     print(read(1))

#     list_all_items()

#    
#     user_value = user_input("Please Enter a value: ")
#     print(user_value)

# Run Tests
test()

#PROGRAM LOOP
running = True
while running:
    selection = user_input("Press A to ADD to list, R to READ from list, U to UPDATE item in list, D to DELETE item in list, P to DISPLAY list, and Q to quit >>")
    running = select(selection)

