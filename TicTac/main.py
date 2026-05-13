import tkinter as tk

# Создаём окно
root = tk.Tk()
root.iconbitmap("icon1.ico")
root.title("Крестики-нолики")

buttons = []  # Сюда будем сохранять все кнопки

# Создаём игровое поле
for i in range(0, 9):  # Создаём 9 кнопок (от 0 до 8)
    button = tk.Button(
        root,
        text="",  # Пока без текста
        font=("Times New Roman", 24),  # Крупный шрифт
        width=5,  # Ширина кнопки
        height=2  # Высота кнопки
    )
    button.grid(row=i//3, column=i%3)  # Размещаем кнопку в сетке
    buttons.append(button)  # Добавляем кнопку в список

# Запускаем программу
root.mainloop()