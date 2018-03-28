# Assignment 1
# ICS3U
# Jazmin M
# March 28, 2018

#uncomment this when you are ready to work on it
def CtoF (celcius):
    """Convert a given celcius temperature to its equivalent farenheit temperature."""
    f=(1.8)*celcius+32
    return int(round(f))


###### uncomment this when you are ready to work on it
def FtoC (farenheit):
    c=(0.55556)*(farenheit-32)
    return int(round(c))

conversion = int(input('Would you like to convert 1) Celcius to Farenheit, or 2) Farenheit to celcius?: '))
if conversion == 1:
    temperature = int(input('Enter your temperature in Celsius: '))
    print(CtoF(temperature))
else:
    temperature = int(input('Enter your temperature in Farenheit: '))
    print(FtoC(temperature))
    
