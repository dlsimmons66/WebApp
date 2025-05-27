import streamlit as st
import myFunctions as functions

# Global Variables
myTasks = functions.openFileRead()


def addNewTask():
    """ Function/Method explanation goes here """
    myTask = st.session_state["new_task"] + "\n"
    print(myTask)
    myTasks.append(myTask)
    print(myTasks)
    functions.openFileWrite(myTasks)


def taskPage():
    """ Function/Method explanation goes here """
    st.title("Daily Task List Web App")
    st.subheader("Task List App")
    st.write("Simple Task List app to improve your productivity.")

    for index, tasks in enumerate(myTasks):
        checkbox = st.checkbox(tasks, key=tasks)
        if checkbox:
            myTasks.pop(index)
            functions.openFileWrite(myTasks)
            del st.session_state[tasks]
            st.rerun()

    st.text_input(label="Add a new Task Item", 
                  label_visibility="hidden", 
                  placeholder="Enter a new task",
                  on_change=addNewTask, 
                  key='new_task')
    
    # st.session_state

if __name__ == "__main__":
    taskPage()
