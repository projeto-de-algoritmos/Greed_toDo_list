import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do List")

def add_task():
    task = entry_task.get()

    listbox_tasks.insert(tkinter.END, task)

def remove_task():
    pass

# GUI
listbox_tasks = tkinter.Listbox(root, height=3, width=50)
listbox_tasks.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Adicionar Tarefa", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tkinter.Button(root, text="Remover Tarefa", width=48, command=remove_task)
button_remove_task.pack()

root.mainloop()