#!/usr/bin/python3

import tkinter as tk


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


# The main application window
def convert_temp():
    temp = float(entry_temp.get())
    from_scale = from_var.get()
    to_scale = to_var.get()

    if from_scale == "C" and to_scale == "F":
        result = celsius_to_fahrenheit(temp)
    elif from_scale == "F" and to_scale == "C":
        result = fahrenheit_to_celsius(temp)
    elif from_scale == "C" and to_scale == "K":
        result = celsius_to_kelvin(temp)
    elif from_scale == "K" and to_scale == "C":
        result = kelvin_to_celsius(temp)
    elif from_scale == "C" and to_scale == "K":
        result = fahrenheit_to_kelvin(temp)

    result_label.config(text=f"Result: {result} {to_scale}")


root = tk.Tk()
root.title("Temperature Converter")


# Input fields and buttons

# Temperature input
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack()

entry_temp = tk.Entry(root)
entry_temp.pack()

# Dropdown for "from scale"
from_var = tk.StringVar(root)
from_var.set("C")  # Default value
from_menu = tk.OptionMenu(root, from_var, "C", "F", "K")
from_menu.pack()

# Dropdown fro "to scale"
to_var = tk.StringVar(root)
to_var.set("F")  # Default value
to_menu = tk.OptionMenu(root, to_var, "C", "F", "K")
to_menu.pack()


# Button to trigger conversion
button_convert = tk.Button(root, text="Convert", command=convert_temp)
button_convert.pack()

# Result display
result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
