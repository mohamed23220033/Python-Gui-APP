import tkinter as tk
import tkinter.messagebox as msg
from tkinter.font import Font
import pickle

#initiating the window
win = tk.Tk()
win.title('Task manager 📝')
win.geometry("600x500")
win.resizable(False,True)
win.configure(background="#6FDCE3")

#-----------------------------------------------------------------------------------------------------

def add_task():

   # Fuction for addding item to the listbox

    if task_input.get() != "":
        lst_tasks.insert(tk.END, task_input.get().capitalize())
        #cpitalize frist element
        entry_task.delete(0, tk.END)
    else:
        msg.showwarning('Waring', 'you must enter a task!')
#-----------------------------------------------------------------------------------------------------        
def clear_tasks():
    lst_tasks.delete(0, tk.END)
#-----------------------------------------------------------------------------------------------------

def search_task():
    keyword = entry_search.get()
    if keyword:
        tasks = lst_tasks.get(0, tk.END)
        matching_tasks = [task for task in tasks if keyword.lower() in task.lower()]
        if matching_tasks:
            msg.showinfo("Matching Tasks", "\n".join(matching_tasks))
        else:
            msg.showinfo("Matching Tasks", "No matching tasks found.")
    else:
        msg.showwarning("Warning", "Please enter a keyword to search!")
#-----------------------------------------------------------------------------------------------------

def del_task():
  
   # Function delete the selected item in the list box 
    try:
        task_index = lst_tasks.curselection()[0]
        lst_tasks.delete(task_index)
    except:
        msg.showwarning('Warning',  'You must select a task to delete!')
#-----------------------------------------------------------------------------------------------------
def load_tasks():
     # Function used to load tasks from the the tasks.dat

    try:

        tasks = pickle.load(open("tasks.dat", "rb"))
        lst_tasks.delete(0,  tk.END)
        if tasks:
            for task in tasks:
                lst_tasks.insert(tk.END, task)
        else:
            msg.showwarning("alert", "no task to be loaded!")
    except:
        msg.showwarning("warning", "No tasks to load")
#-----------------------------------------------------------------------------------------------------
def save_tasks():
# Function used to save tasks to the the tasks.dat
    
    tasks = lst_tasks.get(0, lst_tasks.size())
    if tasks:
        pickle.dump(tasks, open("tasks.dat", "wb"))
    else:
        msg.showwarning('alert', 'nothing to save')
#-----------------------------------------------------------------------------------------------------
#Font
my_font = Font(
    family="Times From Roman",
    size="10",
    weight="bold"
#-----------------------------------------------------------------------------------------------------
)
#storing our entry input
task_input = tk.StringVar()
Todo_label = tk.Label(win, text="notes📝",pady=10 ,height=0, width=70, bg="blue", fg="#EEEEEE",
                       font=("Helvetica", 20), bd=0)
Todo_label.pack()
#-----------------------------------------------------------------------------------------------------
#creating a frame to search
search_frame = tk.Frame(win)
search_frame.pack()
entry_search = tk.Entry(search_frame, width=80)
entry_search.pack(side=tk.LEFT)
bt_search = tk.Button(search_frame, text="⌕",font=('Bold',15), command=search_task,bd=5,bg="#3AA6B9" )
bt_search.pack(side=tk.RIGHT)
#-----------------------------------------------------------------------------------------------------
#creating a frame to pack the list and the scrollbar 
frame = tk.Frame(win)
frame.pack()
lst_tasks = tk.Listbox(frame ,height=20, width=70, font=my_font,selectbackground="cyan" )
lst_tasks.place
lst_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

sc_bar = tk.Scrollbar(frame)
sc_bar.pack(side=tk.RIGHT, fill=tk.BOTH)

lst_tasks.config(yscrollcommand=sc_bar.set)
sc_bar.config(command=lst_tasks.yview)
#-----------------------------------------------------------------------------------------------------
#defining a frame to pack our entry box and add_item button into
iframe = tk.Frame(win)
iframe.pack()

entry_task = tk.Entry(iframe, textvariable=task_input,  width=72)
entry_task.pack(sid=tk.LEFT, fill=tk.BOTH)
entry_task.focus()

#-----------------------------------------------------------------------------------------------------
bt_add = tk.Button(iframe, text="➕",bg='#158aff',fg='white', font=('Bold', 10),height=0, width=8,
                     command=add_task,bd=0,activebackground='#158aff', activeforeground='white' )
bt_add.pack(side=tk.RIGHT, fill=tk.BOTH)
#-----------------------------------------------------------------------------------------------------
bt_save = tk.Button(win, text='Save ', height=0, width=15, command=save_tasks,bg="#06D001" )

bt_save.place(x=40,y=470)
#-----------------------------------------------------------------------------------------------------
bt_load = tk.Button(win,text="load ⬆", height=0, width=15, command=load_tasks,bg="#9BEC00")

bt_load.place(x=175,y=470)
#-----------------------------------------------------------------------------------------------------
bt_del = tk.Button(win, text="    Delete ✖️",height=0, width=15, command=del_task,bg="red")

bt_del.place(x=305,y=470)
#-----------------------------------------------------------------------------------------------------
bt_clear = tk.Button(win, text="Clear ❌",height=0, width=15, command=clear_tasks,bg="brown")

bt_clear.place(x=440,y=470)
#-----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    win.mainloop()


