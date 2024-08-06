import tkinter as tk

# Создаем функции

def add_task():
    task = task_entry.get() # В переменную task мы считываем все что было записано в поле для ввода(task_entry)
    if task: # Если в поле было что-то введено
        task_listBox.insert(tk.END, task) # Добавляем новую задачу в список
        task_entry.delete(0, tk.END)  # Очищаем поле для ввода, в диапазоне от 0 до конца

def delete_task():
    selected_task = task_listBox.curselection()
    selected_task1 = task_listBox2.curselection()
    if selected_task: # Если была выбрана задача
        task_listBox.delete(selected_task) # Удаляем выбранную задачу из списка
    if selected_task1:  # Если была выбрана задача
        task_listBox2.delete(selected_task1)  # Удаляем выбранную задачу из списка

def move_task(from_listbox, to_listbox):
    selected_task = from_listbox.curselection()
    if selected_task: # Если была выбрана задача
        task = from_listbox.get(selected_task) # Получаем текст задачи
        from_listbox.delete(selected_task) # Удаляем задачу из текущего списка
        to_listbox.insert(tk.END, task) # Вставляем задачу в другой список

root = tk.Tk() # Создаём главное окно
root.title("Task list") # Сделаем заголовок окна
root.configure(background='DodgerBlue1') # Установим цвет фона окна

label1 = tk.Label(root, text='Добавьте задачу', bg="DodgerBlue1", fg="white") # Делаем надпись
label1.grid(row=0, column=0, columnspan=2, pady=5) # Добавляем надпись на экран

# В окне создаем поле для ввода, выбираем цвет фона, цвет текста
task_entry = tk.Entry(root, width=30, bg="LightBlue1")
task_entry.grid(row=1, column=0, columnspan=2, pady=10) # Добавляем поле для ввода, делаем отступы

add_task_button = tk.Button(root, text='Добавить задачу', bg="CadetBlue2", command=add_task) # Создаем кнопку
add_task_button.grid(row=2, column=0, columnspan=2, pady=5)

delete_task_button = tk.Button(root, text='Удалить задачу', bg="CadetBlue2", command=delete_task) # Создаем кнопку
delete_task_button.grid(row=3, column=0, columnspan=2, pady=5)

move_button = tk.Button(root, text='Переместить задачу', bg="CadetBlue2", command=lambda: move_task(task_listBox, task_listBox2)) # Создаем кнопку
move_button.grid(row=4, column=0, columnspan=2, pady=5)

label2 = tk.Label(root, text='Список задач:', bg="DodgerBlue1", fg="white") # Делаем надпись
label2.grid(row=6, column=0, pady=5)

label3 = tk.Label(root, text='Список выполненных задач:', bg="DodgerBlue1", fg="white") # Делаем надпись
label3.grid(row=6, column=1, pady=5) # Добавляем надпись на экран

task_listBox = tk.Listbox(root, width=50, height=10, bg="LightBlue1") # Создаем список для отображения задач
task_listBox.grid(row=7, column=0, padx=10)

task_listBox2 = tk.Listbox(root, width=50, height=10, bg="LightBlue1") # Создаем список для отображения задач
task_listBox2.grid(row=7, column=1, padx=10)

root.mainloop() # Для того, чтобы окно не исчезало, пока мы его не закроем
