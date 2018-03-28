# Assignment 1
# ICS3U
# Jazmin M
# March 28, 2018

#uncomment this when you are ready to work on it
def CtoF (celcius):
    """Convert a given celcius temperature to its equivalent farenheit temperature."""
    f=(1.8)*celcius+32
    return(round(f,0))


###### uncomment this when you are ready to work on it
#def FtoC ():

temperature = int(input('Enter your temperature in Celsius: '))
print(CtoF(temperature))
