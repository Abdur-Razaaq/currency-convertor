# importing all necessary modules from python library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

# initialising window. Setting name, size and background color
root = Tk()
root.title('Currency Convertor')
root.geometry("280x500")
root.config(bg="Blue")

# Creating notebook format
my_notebook = ttk.Notebook(root)
my_notebook.place(x=20, y=20)

# requesting
information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

# # Getting conversion rates
conversion_rate = information_json['conversion_rates']

# creating, sizing and coloring frames
currency_frame = Frame(my_notebook, width=480, height=480, bg="teal")
convertor_frame = Frame(my_notebook, width=480, height=480, bg="teal")

# packing frames
currency_frame.pack(fill="both", expand=1)
convertor_frame.pack(fill="both", expand=1)

# naming frames
my_notebook.add(currency_frame, text='Currencies')
my_notebook.add(convertor_frame, text='Conversions')

# label frames. setting color and packing
home = LabelFrame(currency_frame, text="Conversion from USD", bg="teal")
home.pack(pady=20)

# creating and packing entry
home_entry = Entry(home, font=24)
home_entry.pack(padx=10, pady=10)

# Creating and packing label frame
conversion = LabelFrame(currency_frame, text='Conversion Currency', bg="teal")
conversion.pack(pady=20)

# creating and packing label. adding font and bg color
convert = Label(conversion, text="Convert To: ", font=("Arial", 20))
convert.config(bg="teal")
convert.pack()

# creating, sizing and packing conversion list
convert_list = Listbox(conversion, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.pack()

# creating, setting size, font and packing convert label
convert_label = Label(convertor_frame, text="Converted to: ", font=("Roboto", 20))
convert_label.config(bg="teal")
convert_label.pack()


# Function that converts currencies using requested information
def convert_currency():
    try:
        num = float(home_entry.get())
        print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
        ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
        convert_label['text'] = ans
        my_notebook.select(1)
    except ValueError:  # error catching
        messagebox.showerror("Error", "PLease Enter a Number")
    except requests.exceptions.ConnectionError as error:
        messagebox.showerror("Error", "No Internet Connection")


# buttons
convert_btn = Button(currency_frame, command=convert_currency, text="Convert", font=("Arial", 20), width=10)
convert_btn.config(bg="teal")
convert_btn.pack()

# Keeps window open until terminated by user
root.mainloop()
