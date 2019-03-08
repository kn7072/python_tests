from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title('Калькулятор')

btn_list = [
    '7', '8', '9', 'C', '√',
    '4', '5', '6', '-', '*',
    '1', '2', '3', '+', '/',
    '0', '00', '.', '=', 'OFF'
]

input_flag = True


def calc(key):
    to_print = '00123456789+-*/.'
    calc = '+-/*'
    if key == '=':
        global input_flag
        input_flag = False
        if calc_entry.get():
            try:
                result = eval(calc_entry.get())
                result_entry.insert(END, str(result))
            except ZeroDivisionError:
                messagebox.showerror('Ошибка', 'На ноль делить нельзя')
                calc_entry.delete(0, 100)
                result_entry.delete(0, 100)
            except:
                messagebox.showerror('Ошибка', 'Проверьте правильность данных')
                calc_entry.delete(0, 100)
                result_entry.delete(0, 100)
        else:
            messagebox.showerror('Ошибка', 'ЭЭЭЭй! Тут пусто')
    if key == 'C':
        calc_entry.delete(0, 100)
        result_entry.delete(0, 100)
    if key in to_print:
        if not input_flag:
            calc_entry.delete(0, 100)
            result_entry.delete(0, 100)
        input_flag = True
        calc_entry.insert(END, key)
    if key == '√':
        try:
            num = int(calc_entry.get())
            result = math.sqrt(num)
            result_entry.insert(END, result)
        except:
            messagebox.showerror('Ошибка', 'Проверьте правильность данных')
    if key == 'OFF':
        root.quit()



r = 1
c = 0

for button in btn_list:
    cmd = lambda x=button: calc(x)
    ttk.Button(root, text=button, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1


def delete_one():  # Кнопка удаления по одному элементу
    text_enter = calc_entry.get()[0:-1]
    calc_entry.delete(0, 100)
    calc_entry.insert(END, text_enter)



cmd1 = lambda: delete_one()

ttk.Button(root, text='<-', command=cmd1).grid(row=1, column=5, columnspan=30)

calc_entry = Entry(root, width=20)
result_entry = Entry(root, width=15)
calc_entry.grid(row=0, column=0, columnspan=3)
result_entry.grid(row=0, column=3, columnspan=3)
def de():
    parse = calc_entry.get()
    for i in parse:
        if i in calc:
            try:
                if calc_entry.get():
                    result_entry.delete(0, 100)
                    result_entry.insert(END, eval(calc_entry.get()))
            except:
                result_entry.delete(0, 100)
                pass
de()

root.mainloop()
