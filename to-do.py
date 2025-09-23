input_user = ''
list_of_tasks = []
while input_user != 'exit':
    input_user = input("Enter a task to add to your to-do List (or type 'exit' to finish): ")
    list_of_tasks.append(input_user)
    if input_user == 'exit':
        list_of_tasks.remove('exit')
        break
# for task in list_of_tasks:
#     print(f'{task} is on your to-do list.')
# print("Your to-do list is complete!")
def printTask():
    for index, task in enumerate(list_of_tasks):
        print(index + 1, task)
    print("Your to-do list is complete!")

printTask()

delete_option = ''    
while delete_option != 'n':
    delete_option = input('Do you eliminate a task? (y/n) ')
    
    if delete_option == 'y':
        try: 
            delete= int(input('Choose number to delete item: '))
            
            if 0 < delete < len(list_of_tasks):
                delete -= 1
                del list_of_tasks[delete]
            else: 
                print('Out of range')
        except ValueError:
            print('Is a number not a letter')
printTask()
