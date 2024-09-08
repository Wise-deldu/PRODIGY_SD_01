#!/usr/bin/python3

import argparse


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


# Code to handle argparse command-line arguments

def parse_args():
    parser = argparse.ArgumentParser(description="Temperature Converter")
    parser.add_argument(
        "temp",
        type=float,
        help="Temperatuerure to convert"
    )
    parser.add_argument(
        "from_scale",
        type=str,
        choices=["C", "F", "K"],
        help="Scale to convert from"
    )
    parser.add_argument(
        "to_scale",
        type=str,
        choices=["C", "F", "K"],
        help="Scale to convert to")
    return parser.parse_args()


# The logic to call the appropriate conversion function
def convert_temperature(temp, from_scale, to_scale):
    if from_scale == "C" and to_scale == "F":
        return celsius_to_fahrenheit(temp)
    elif from_scale == "F" and to_scale == "C":
        return fahrenheit_to_celsius(temp)
    elif from_scale == "C" and to_scale == "K":
        return celsius_to_kelvin(temp)


if __name__ == "__main__":
    args = parse_args()
    result = convert_temperature(args.temp, args.from_scale, args.to_scale)
    print(f"{args.temp} {args.from_scale} is {result} {args.to_scale}")
