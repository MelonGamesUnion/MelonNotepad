import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Блокнот")
        self.root.geometry("600x400")
        self.textarea = tk.Text(self.root, font=("Helvetica", 12))
        self.textarea.pack(fill="both", expand=True)
        
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Открыть", command=self.open_file)
        self.filemenu.add_command(label="Сохранить", command=self.save_file)
        self.filemenu.add_command(label="Сохранить как", command=self.save_file_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Выход", command=self.exit_application)
        self.menubar.add_cascade(label="Файл", menu=self.filemenu)
        
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Вырезать", command=self.cut_text)
        self.editmenu.add_command(label="Копировать", command=self.copy_text)
        self.editmenu.add_command(label="Вставить", command=self.paste_text)
        self.menubar.add_cascade(label="Редактировать", menu=self.editmenu)
        
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="О программе", command=self.show_about)
        self.menubar.add_cascade(label="Помощь", menu=self.helpmenu)
        
        self.root.config(menu=self.menubar)
    
    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "r") as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.END, file.read())
    
    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))
            messagebox.showinfo("Сохранение файла", "Файл успешно сохранен.")
    
    def save_file_as(self):
        filepath = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))
            messagebox.showinfo("Сохранение файла", "Файл успешно сохранен.")
    
    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")
    
    def show_about(self):
        messagebox.showinfo("О программе", "Простой блокнот на Python Tkinter.")
    
    def exit_application(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
