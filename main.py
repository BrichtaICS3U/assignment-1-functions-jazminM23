# Assignment 1
# ICS3U
# Jazmin M
# March 28, 2018

#uncomment this when you are ready to work on it
def CtoF (celsius):
    """Convert a given celsius temperature to its equivalent farenheit temperature."""
    f=(1.8)*celsius+32
    return int(round(f))


###### uncomment this when you are ready to work on it
def FtoC (farenheit):
    c=(0.55556)*(farenheit-32)
    return int(round(c))

conversion = int(input('Would you like to convert 1) Celsius to Farenheit, or 2) Farenheit to celsius?: '))
if conversion == 1:
    temperature = int(input('Enter your temperature in Celsius: '))
    if temperature <-273:
        print ('Invalid temperature: It is impossible to have a temperature below -273 Celsius.')
    else:
        print(CtoF(temperature))
else:
    temperature = int(input('Enter your temperature in Farenheit: '))
    if temperature <-460:
        print('Invalid temperature: It is impossible to have a temperature below -460 Farenheit.')
    else:
        print(FtoC(temperature))
    
