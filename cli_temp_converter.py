#!/usr/bin/env python3


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


# The logic to call the appropriate conversion function
def convert_temperature(temp, from_scale):
    if from_scale == "C":
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is {fahrenheit}°F and {kelvin}K")
    elif from_scale == "F":
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is {celsius:.2f}°C and {kelvin:.2f}K")
    elif from_scale == "K":
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")


def main():
    while True:
        try:
            user_input = input("Enter the temperature and scale"
                               "(e.g., '37 C'): ").strip()

            args = user_input.split()

            if len(args) != 2:
                print("Invalid input. Please provide temperature and "
                      "scale in the format 'temp scale' (e.g., '37 C') "
                      "or Ctrl+D to exit.")
                continue

            try:
                temp = float(args[0])
            except ValueError:
                print("Invalid temperature. Please enter a numeric value "
                      "or Ctrl+D to exit.")
                continue

            from_scale = args[1].upper()

            if from_scale not in ["C", "F", "K"]:
                print("Invalid temperature scale. Use 'C' for Celsius, "
                      "'F' for Fahrenheit, or 'K' for Kelvin.")
            else:
                convert_temperature(temp, from_scale)
                break
        except EOFError:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
