def celsius_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit

while True:
    try:
        celsius_degree = int(input('Enter a number for Celsius degree to Fahrenheit: '))
        break
    except ValueError:
        print('A number not a letter')
    
fahrenheit_degree = celsius_fahrenheit(celsius_degree)
print(fahrenheit_degree)
