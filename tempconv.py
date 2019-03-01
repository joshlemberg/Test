# tempconv.py
# Temperature Converter
# This code converts temperature from Celsius to Farenheight

def main():
    unit = input("Is your temperature in Celsius, Kelvin, or Fahrenheit? " )
    desired = input("Is your desired unit Celsius, Kelvin, or Fahrenheit? " )
    if unit in ["Celsius", "celsius"]:
        celsius = float(input("What is the temperature in Celsius? "))
        if desired == "Celsius":
            print("The temperature is", celsius,"°C")
            return
        if desired == "Fahrenheit":
            fahrenheit = (9/5) * celsius + 32
            print("The temperature is", fahrenheit, "°F.")
            return
        if desired == "Kelvin":
            kelvin = celsius + 273.15
            print("The temperature is", kelvin, "K.")
            return
    if unit == "Fahrenheit":
        fahrenheit = float(input("What is the temperature in Fahrenheit? "))
        if desired == "Celsius":
            celsius = fahrenheit * 1.8 + 32
            print("The temperature is", celsius,"°C.")
            return
        if desired == "Fahrenheit":
            print("The temperature is", fahrenheit,"°F.")
            return
        if desired == "Kelvin":
            kelvin = (fahrenheit + 459.67) * (5/9)
            print("The temperature is", kelvin, "K.")
            return
    if unit == "Kelvin":
        kelvin = float(input("What is the temperature in Kelvin? "))
        if desired == "Celsius":
            celsius == kelvin - 273.15
            print("The temperature is", celsius,"°C.")
            return
        if desired == "Fahrenheit":
            fahrenheit = kelvin * 1.8 - 459.67
            print("The temperature is", fahrenheit,"°F.")
            return
        if desired == "Kelvin":
            print("The temperature is", kelvin, "K.")       



main()
    
