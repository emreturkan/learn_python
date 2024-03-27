  
  
todos =[]

while True:
    user_action =  input("Type add,show, edit or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case "add": 
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)
        case "show":
            for index,item in enumerate(todos):
                print(f"{index+1}-{item}")
        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1
            todos[number] = input("Enter new todo: ")
            print(todos[number])
        case "complete":
            number = int(input("Number of todo to complete: "))
            number = number - 1
            todos.remove(todos[number])
        case "exit":
            break
        case _:
            print("Unknown command")