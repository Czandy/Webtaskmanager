import streamlit  as st
import functionss
from datetime import datetime

now = datetime.now()
xnow = now.strftime("%x, %H:%M")
tasks = functionss.get_tasks()
completetasks = functionss.get_completetasks()

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functionss.write_tasks(tasks)
    st.session_state["new_task"] = ""


st.title("Task Manager")
st.subheader("This is your new task manager")
st.write("Use this web application to create and keep track of your tasks.")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        completetasks.append(f'**{task.strip()}** - Time of completion: {xnow}')  # Append the completed task
        functionss.write_completetasks(completetasks)  # Save completed tasks

        tasks.pop(index)  # Remove from tasks list
        functionss.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label='x',label_visibility='hidden', placeholder='Add new tasks here..',
              on_change=add_task, key="new_task")

st.divider()

st.subheader(''':red[*Completed Tasks*]''')
for index, completedtask in enumerate(completetasks):
    st.text(completedtask)

Delete = st.button("Delete all tasks permanently", type="primary")
if Delete:
    open('donetasks.txt', 'w').close()
    st.rerun()


