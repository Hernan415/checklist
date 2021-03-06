#Create our Checklist
checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#def mark_completed(index):
#    index = 0
#    for list_item in Checklist:
#        checklist.append('√' + Checklist)
def select(function_code):

    if function_code.upper() == "C":
        #Create item in checklist here
        input_item = user_input("Input item:")
        create(item)
    elif function_code.upper() == "R":
        item_index = user_input("Index Number?")
        # Read item in checklist here
        read(item_index)
    elif function_code.upper() == "P":
        # Print all items here
        list_all_items()
    elif function_code.upper() == "Q":
        # This is where we want to stop our loop
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

item = user_input("Please Enter an Item: ")
print(item)
#def test():
#    create("purple sox")
#    create("red cloak")
#
#    print(read(0))
#    print(read(1))
#
#    update(0, "purple socks")
#
#    destroy(1)
#
#    print(read(0))
#
#    mark_completed(1)
#
#    list_all_items()
#     # Call your new function with the appropriate value
#    select("C")
#    # View the results
#    list_all_items()
#    # Call function with new value
#    select("R")
#    # View results
#    list_all_items()
#    # Continue until all code is run
#
#test()
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)
