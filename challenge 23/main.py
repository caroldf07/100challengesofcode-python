from tkinter import *

"""Um dos aprendizados mais profundos nesse chalenge, foi a questão do grid.
O python quebra se tu tenta fazer algo do tipo Label(text="Miles").grid(column=2, row=0). 
Primeiro o python instancia o objeto, popula e somente depois ele monta o grid.
"""

def converter():
    converted = float(value.get()) * 1.609344
    km_converted.config(text=f"{converted}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=200)
window.config(padx=50, pady=100)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0, row=1)

km_converted = Label(text="0")
km_converted.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

value = Entry(width=10)
value.grid(column=1, row=0)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

window.mainloop()
