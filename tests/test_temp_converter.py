import pytest
from temp_converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15
    assert celsius_to_kelvin(-273.15) == 0


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40


def test_fahrenheit_to_kelvin():
    assert pytest.approx(fahrenheit_to_kelvin(32), 0.01) == 273.15
    assert pytest.approx(fahrenheit_to_kelvin(212), 0.01) == 373.15
    assert pytest.approx(fahrenheit_to_kelvin(-40), 0.01) == 233.15


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(373.15) == 100
    assert kelvin_to_celsius(0) == -273.15


def test_kelvin_to_fahrenheit():
    assert pytest.approx(kelvin_to_fahrenheit(273.15), 0.01) == 32
    assert pytest.approx(kelvin_to_fahrenheit(373.15), 0.01) == 212
    assert pytest.approx(kelvin_to_fahrenheit(233.15), 0.01) == -40
