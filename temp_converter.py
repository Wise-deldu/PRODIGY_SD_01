#!/usr/bin/env python3

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67


def main():
    print("Temperature Conversion Program")
    print("-------------------------------")

    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid temperature value. Please enter a numerical value.")
        return

    primary_unit = input("Enter the original unit "
                         "(Celsius, Fahrenheit, or Kelvin): ").strip().lower()

    if primary_unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
    elif primary_unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
    elif primary_unit == "kelvin":
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
    else:
        print("Invalid unit. Please enter 'Celsius', "
              "'Fahrenheit', or 'Kelvin'.")
        return

    print(f"{temp} {primary_unit.capitalize()} is equivalent to:")
    if primary_unit != "fahrenheit":
        print(f"{fahrenheit:.2f} °F")
    if primary_unit != "kelvin":
        print(f"{kelvin:.2f} K")
    if primary_unit != "celsius":
        print(f"{celsius:.2f} °C")


if __name__ == "__main__":
    main()
