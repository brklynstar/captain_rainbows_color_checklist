# Create our Checklist
print()
checklist = list()

# Define Functions
#Create function is going to add the input of item and append it to the checklist
def create(item):
  checklist.append(item)

# Read function will return the value that lives at that index in our checklist and save it in item
def read(index):
    return checklist[index]

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


# def mark_completed(index):
#     checklist.append("√" + index)
#     return mark_completed


def select(function_code):
    #ADD ITEM
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)
    
    #READ ITEM
    elif function_code == "R":
        item_index = user_input("Index Number? ")
        read(int(item_index))

    #UPDATE ITEM
    elif function_code == "U":
        read(item_index) 

    #DESTROY ITEM
    elif function_code == "D":
        read(item_index)

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


def user_input(prompt):
    user_input = input(prompt)
    return user_input

#PROGRAM LOOP
running = True
while running:
    selection = user_input("Press A to ADD to list, R to READ from list, U to UPDATE item in list, D to DELETE item in list, P to DISPLAY list, and Q to quit >>")
    running = select(selection)

# #TEST
# def test():

#     create("Purple sox")
#     create("red cloak")

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

# # Run Tests
#     test()

