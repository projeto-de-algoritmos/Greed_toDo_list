import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To Do List")

tasks = []  # Lista para armazenar as tarefas adicionadas
end_time_list = []

def add_task():
    task = entry_task.get()
    end_time = entry_end_time.get()
    print(end_time)
    if task != "" and end_time != "":
        for item in end_time_list:
            if end_time == item:
                tkinter.messagebox.showwarning(title="Atenção!", message="Já existe uma tarefa com a mesma data de término")
                return
        task_with_end_time = task + " (Término: " + end_time + ")"
        tasks.append(task_with_end_time)
        tasks.sort(key=lambda x: x.split(" (Término: ")[-1][:-1])  # Ordena as tarefas com base no tempo de término
        update_listbox()
        entry_task.delete(0, tkinter.END)
        entry_end_time.delete(0, tkinter.END)
        end_time_list.append(end_time)
    else:
        tkinter.messagebox.showwarning(title="Atenção!", message="Insira uma tarefa e um tempo de término")

def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_listbox()

def update_listbox():
    listbox_tasks.delete(0, tkinter.END)
    for task in tasks:
        listbox_tasks.insert(tkinter.END, task)

# GUI
frame_tasks = tkinter.Frame()
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks)

frame_entry = tkinter.Frame()
frame_entry.pack()

label_task = tkinter.Label(frame_entry, text="Tarefa:")
label_task.pack(side=tkinter.LEFT)

entry_task = tkinter.Entry(frame_entry, width=30)
entry_task.pack(side=tkinter.LEFT)

label_end_time = tkinter.Label(frame_entry, text="Término:")
label_end_time.pack(side=tkinter.LEFT)

entry_end_time = tkinter.Entry(frame_entry, width=10)
entry_end_time.pack(side=tkinter.LEFT)

button_add_task = tkinter.Button(root, text="Adicionar Tarefa", width=48, command=add_task)
button_add_task.pack()

button_remove_task = tkinter.Button(root, text="Remover Tarefa", width=48, command=remove_task)
button_remove_task.pack()

root.mainloop()