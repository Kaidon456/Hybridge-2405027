# main.py
import tkinter as tk
from tkinter import ttk

# Para una mejor organización y modularidad, encapsulamos
# toda la lógica de la aplicación en una clase.
class TaskListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task List App")
        self.geometry("450x400")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")  # Usamos un tema moderno

        # Crear el frame principal para contener todos los widgets
        self.main_frame = ttk.Frame(self, padding="15 15 15 15")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Configurar el diseño responsive para la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Crear los widgets y la interfaz
        self.create_widgets()

    def create_widgets(self):
        # 1. Entrada de texto y botón para añadir tareas
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        self.task_entry = ttk.Entry(self.input_frame, font=("Arial", 14), width=35)
        self.task_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.add_button = ttk.Button(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        # Configurar responsive para el frame de entrada
        self.input_frame.grid_columnconfigure(0, weight=1)

        # 2. Listbox para mostrar las tareas
        # Usamos un Frame con un Scrollbar para una mejor experiencia de usuario
        self.list_frame = ttk.Frame(self.main_frame)
        self.list_frame.grid(row=1, column=0, sticky="nsew")

        self.task_list = tk.Listbox(
            self.list_frame, 
            height=10, 
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            activestyle="none"
        )
        self.task_list.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.task_list.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.task_list['yscrollcommand'] = self.scrollbar.set

        # Configurar responsive para la lista
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_rowconfigure(0, weight=1)

        # 3. Botones de acción
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.grid(row=2, column=0, pady=(10, 0), sticky="ew")
        
        self.complete_button = ttk.Button(self.button_frame, text="Complete", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill="x")

        self.delete_button = ttk.Button(self.button_frame, text="Delete", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, expand=True, fill="x")

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_list.curselection()
            if selected_index:
                self.task_list.delete(selected_index)
        except tk.TclError:
            pass  # No hay selección, no hacer nada

    def complete_task(self):
        try:
            selected_index = self.task_list.curselection()
            if selected_index:
                task = self.task_list.get(selected_index)
                # Remueve la tarea y la re-inserta al final con un formato diferente
                self.task_list.delete(selected_index)
                self.task_list.insert(tk.END, f"✔️ {task}")
                # Cambia el color del fondo para indicar que está completada
                self.task_list.itemconfig(tk.END, {'bg': '#d4edda', 'fg': '#155724'})
        except tk.TclError:
            pass # No hay selección, no hacer nada

# Ejecutar la aplicación
if __name__ == "__main__":
    app = TaskListApp()
    app.mainloop()