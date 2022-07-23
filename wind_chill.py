def wind_chill(data, data2):
    temperature = int(data)
    if data2 == "F":
        for i in range(5, 65, 5):
            wind_speed = i
            v = wind_speed
            wc = 35.74 + 0.6215 * temperature - 35.75 * (v ** 0.16) + 0.4275 * temperature * (v ** 0.16)
            print(f"At temperature {temperature}F, and wind speed {v}mph, the windchill is: {wc:.2f}F")
    elif data2 == "C":
        for i in range(5, 65, 5):
            wind_speed = i
            v = wind_speed
            #The windchill formula for celsius (https://sciencing.com/calculate-wind-chill-factor-5981683.html)
            wc = 13.12 + 0.6215 * temperature - 11.37 * (v ** 0.16) + 0.3965 * temperature * (v ** 0.16)
            print(f"At temperature {temperature}C, and wind speed {v}km/h, the windchill is: {wc:.2f}C")


user_choose = int(input("What is the temperature? "))
user_choose_temperature = input("Fahrenheit or Celsius (F/C)? ")
wind_chill(user_choose, user_choose_temperature)







