'''
This is referred to as a module and is imported into the main function
via the import command. 
'''

'''
var1 = openFileRead()
In this module the filepath is set as the default and is not required to be
passed to the module from within the main program. In order to access the 
list information the user must assign the results to var1
'''
FILEPATH = "./"

def openFileRead(file_path=FILEPATH):
    with open(file_path + 'tasks.txt', 'r') as read_file:
        local_tasks = read_file.readlines()
    return(local_tasks)


'''
var1 = openFileWrite(tasks)
In this module the filepath is set as the default and a 'task' list is required 
to be passed to the module from within the main program. There is no data to be
returned so the function acts like a procedure
'''

def openFileWrite(wrt_tasks, file_path=FILEPATH):
    with open(file_path + 'tasks.txt', 'w') as write_file:
        write_file.writelines(wrt_tasks)


if __name__ == '__main__':
    msg = openFileRead()
    print(msg)
