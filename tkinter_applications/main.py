from tkinter import *
from tkinter import messagebox
from time import *
def calc_age():
    t = time()
    y = int(hy.get())
    m = int(hm.get())
    d = int(hd.get())
    o=0
    y1 = 0
    m1 = 0
    d1 = 0
    o = int(t) - y*365*24*60*60+m*31*24*60*60+d*24*60*60
    messagebox.showinfo("age", f"Вам {o//(365*24*60*60)} лет, {o/(31*24*60*60)} месяцев, {o/(24*60*60)} дней")
def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 4)

    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ {bmi} соответствует недостаточной массе')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ {bmi} соответствует нормальной массе')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ {bmi} соответствует избыточной массе')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ {bmi} соответствует ожирению')


window = Tk()
window.title('Калькулятор индекса массы тела (ИМТ) или подробный расчёт возраста')
window.geometry('1000x1000')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

cy = Label(
    frame,
    text="Год:"
)
cy.grid(row=2, column=3)
hy = Entry(
    frame,
)
hy.grid(row=2, column=4)

cm = Label(
    frame,
    text="Месяц:"
)
cm.grid(row=3, column=3)
hm = Entry(
    frame,
)
hm.grid(row=3, column=4)

cd = Label(
    frame,
    text="День:"
)
cd.grid(row=4, column=3)
hd = Entry(
    frame,
)
hd.grid(row=4, column=4)

c_btn = Button(
    frame,
    text='Рассчитать возраст',
    command=calc_age
)
c_btn.grid(row=5, column=4)

height_lb = Label(
    frame,
    text="Введите свой рост (в см)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Введите свою массу (в кг)  ",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,
    text='Рассчитать ИМТ',
    command=calculate_bmi
)
cal_btn.grid(row=5, column=2)

window.mainloop()