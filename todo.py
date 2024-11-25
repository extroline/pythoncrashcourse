#Output the list of things today
#Ask the user if it's done 
# If stateent if done remove otherwise keep

#make sure totos.txt exists 
#read todos from todos.txt as a list of strings. Each line should have its own element in the list.

# for loop through the list 
    # print the to-do
    # ask the user if they completed this 
        # remove it
    # else
        # keep it

f = open("totos.txt", "r")
content = f.read()
print(content.split("\n"))
f.close()

todo_list = content.split("\n")
remaining_todo_list = []
print("My list:", todo_list)

for todo in todo_list:
    print(todo)
    user_input = input("Completed? (y/n)")
    if user_input != "y":
        remaining_todo_list.append(todo)

while True:
    new_todo = input("Add todo (q to quit)")
    if new_todo == "q":
        break
    else:
        remaining_todo_list.append(new_todo)

with open("totos.txt", "w") as f:
    output = "\n" .join(remaining_todo_list)
    f.write(output)

'''def get_user_input():
    vaild_input = False 
    while not vaild_input: 
        user_input = input(my_list)
        if user_input == "q":
            return user_input
        elif user_input == my_list[0] or user_input == "1" or user_input == "2":
            vaild_input = True 
            return int(user_input)
        else:
            print("Invaild Input! Read the directions and try")
'''

#user_input = get_user_input()

# while loop 
    # ask for the another to-do 
    # if they input "q", 
        # quit out with "break" 
    # else 
        # add to to-do list


# write new todos to file 