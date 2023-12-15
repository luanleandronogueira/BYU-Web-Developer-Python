# function

#function to convert F° at C°
def convert_c_f(celsius):
    F = (celsius * 9/5) + 32 # formula °F = (°C * 9/5) + 32
    return F

#function to convert C° at F°
def convert_f_c(fahrenheit):
    C = (fahrenheit - 32) * 5/9 # Formula °C = (°F - 32) * 5/9
    return C

# Wind Chill = 13.12 + 0.6215 * T - 11.37 * V^0.16 + 0.3965 * T * V^0.16
#  wind_chill = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)

def windchill(wind):
    
    for i in mph:

        Wind = 13.12 + 0.6215 * wind - 11.37 * (i ** 0.16) + 0.3965 * wind * (i** 0.16)
        # Wind = wind - (i * 0.7)
        print(f'At temperature {weather} .F°, and wind speed {i} mph, the windchill is: {Wind:.2f}') 
          
    return Wind

def windchill_f(wind_f):
    for i in mph:
        Wind_f = 13.12 + 0.6215 * wind_f - 11.37 * (i ** 0.16) + 0.3965 * wind_f * (i** 0.16)
        print(f'At temperature {we_f} .F°, and wind speed {i} mph, the windchill is: {Wind_f:.2f}') 
    return

c = 'c'
f = 'f'

mph = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

weather = float(input('What is the temperature? '))

weather_Type = input('Fahrenheit or Celsius (F/C)? ')

if weather_Type.lower() == 'f':
    
    # the function will print the return
    we = windchill(weather)


# finalizar essa função

if weather_Type.lower() == 'c':
    
    convert_weather = convert_c_f(weather)
    
    we_f = windchill(convert_weather)






