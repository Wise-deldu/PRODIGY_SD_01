#!/usr/bin/python3

from flask import Flask, request, render_template, flash  # type: ignore
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages


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


@app.route("/", methods=["GET", "POST"])
def convert_temp():
    result = None
    error = None
    if request.method == "POST":
        try:
            temp = float(request.form["temp"])
            from_scale = request.form["from_scale"]
            to_scale = request.form["to_scale"]

            if from_scale == "C" and to_scale == "F":
                result = celsius_to_fahrenheit(temp)
            elif from_scale == "F" and to_scale == "C":
                result = fahrenheit_to_celsius(temp)
            elif from_scale == "C" and to_scale == "K":
                result = celsius_to_kelvin(temp)
            elif from_scale == "K" and to_scale == "C":
                result = kelvin_to_celsius(temp)
            elif from_scale == "F" and to_scale == "K":
                result = fahrenheit_to_kelvin(temp)
            elif from_scale == "K" and to_scale == "F":
                result = kelvin_to_fahrenheit(temp)
            else:
                error = "Invalid conversion scales selected."
        except (ValueError, KeyError):
            error = "Invalid input. Please enter a valid number."

    return render_template("index.html", result=result, error=error)
