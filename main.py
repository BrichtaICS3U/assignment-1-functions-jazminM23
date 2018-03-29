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

#continueConversion= int(input('Would you like to do another temperature conversion? 1) YES 2) NO'))
#^need to ask this question only after first conversion^
continueConversion= 1
while continueConversion== 1:
    #^this also allows any number other than one to stop program, not just 2
    conversion = int(input('Would you like to convert 1) Celsius to Farenheit, or 2) Farenheit to celsius?: '))
    if conversion == 1:
        temperature = int(input('Enter your temperature in Celsius: '))
        if temperature <-273:
            print ('Invalid temperature: It is impossible to have a temperature below -273 Celsius.')
            continueConversion=int(input('Would you like to do another temperature conversion? 1) YES 2) NO')) 
        else:
            print(CtoF(temperature))
            continueConversion=int(input('Would you like to do another temperature conversion? 1) YES 2) NO')) 
    elif conversion ==2:
        temperature = int(input('Enter your temperature in Farenheit: '))
        if temperature <-460:
            print('Invalid temperature: It is impossible to have a temperature below -460 Farenheit.')
            continueConversion=int(input('Would you like to do another temperature conversion? 1) YES 2) NO'))
        else:
            print(FtoC(temperature))
            continueConversion=int(input('Would you like to do another temperature conversion? 1) YES 2) NO'))   
    else:
        print('Not a valid choice. Please pick a number from given options.')

    #continueConversion=int(input('Would you like to do another temperature conversion? 1) YES 2) NO'))
