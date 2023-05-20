import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Insira uma tarefa")

def remove_task():
    task_index = listbox_tasks.curselection()
    listbox_tasks.delete(task_index)

# GUI
frame_tasks = tkinter.Frame()
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Adicionar Tarefa", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tkinter.Button(root, text="Remover Tarefa", width=48, command=remove_task)
button_remove_task.pack()

root.mainloop()