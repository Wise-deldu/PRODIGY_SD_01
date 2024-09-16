# Temperature Conversion Program

## Description
* A Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin. 
* The program includes functions for each type of conversion and uses `pytest` for unit testing to ensure accuracy and reliability. 
* Additionally, `pycodestyle` is used to enforce `PEP 8` style guidelines for clean and readable code.

## Features
- Converts temperatures between:
  - Celsius to Fahrenheit
  - Celsius to Kelvin
  - Fahrenheit to Celsius
  - Fahrenheit to Kelvin
  - Kelvin to Celsius
  - Kelvin to Fahrenheit
- Input validation and error handling for incorrect inputs.
- Modular code design for easy maintenance and reusability.
- Unit tests using `pytest` to ensure correctness.
- Code adheres to PEP 8 style guidelines, checked with `pycodestyle`.

## Requirements
* Python 3.x
* `pytest` (for running tests)
* `pycodestyle` (for checking code style)


## Usage

### Running the Program
1. **Clone this repository:**
   ```bash
   git clone https://github.com/Wise-deldu/PRODIGY_SD_01
   cd PRODIGY_SD_01
2. **Run the program:**
```
python3 temp_converter.py
```

3. The program will prompt you to input a temperature and select the original unit (Celsius, Fahrenheit, or Kelvin). It will then display the equivalent values in the other units.

**Example:**
```
Enter the temperature value: 100
Enter the original unit (Celsius, Fahrenheit, or Kelvin): celsius
100 Celsius is equivalent to:
212.00 °F
373.15 K
```
4. Testing the Program
To run the unit tests using `pytes`t, first `install pytest` if you don't have it:
```
pip3 install pytest
```
Run the tests with:
```
pytest test_temp_converter.py
```

**Style Guide Enforcement with pycodestyle**
This project follows the `PEP 8` style guide. You can check for any style violations using pycodestyle.

**Install `pycodestyle`:**
```
pip install pycodestyle
```
Run pycodestyle on your Python files:
```
pycodestyle temp_converter.py
pycodestyle test_temp_converter.py
```

