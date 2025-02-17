import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        self.load_tasks()
        
        self.title_label = tk.Label(root, text="Task Title:")
        self.title_label.pack()
        
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack()
        
        self.complete_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.complete_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
        self.display_tasks()
    
    def add_task(self):
        title = self.title_entry.get().strip()
        if title:
            self.tasks.append({"title": title, "completed": False})
            self.title_entry.delete(0, tk.END)
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty!")
    
    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")
    
    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")
    
    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[X]" if task["completed"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")
    
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
