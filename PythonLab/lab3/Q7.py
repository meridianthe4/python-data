# Q.7
# Following data displays min/max/average temp for cities
# weather= [{'Mumbai' : [28, 30, 32]},.....]

# 1. Print the weather data
# 2. Print the city with maximum/min temp
# 3. Print all the cities that expereince min temp more than 30 degree
# 4. Create a dictionary to print 'City':'Ave temp'


weather = [
    {'Mumbai': [28, 30, 32]},
    {'Delhi': [25, 29, 35]},
    {'Chennai': [32, 34, 36]},
    {'Bangalore': [20, 25, 30]},
    {'Pune': [22, 27, 31]}
]


# 1. Print weather data
print("Weather Data:")
for record in weather:
    for city, temps in record.items():
        print(f"{city}: Min={temps[0]}, Avg={temps[1]}, Max={temps[2]}")


# 2. City with max/min temp
max_city = min_city = None
max_temp, min_temp = float('-inf'), float('inf')

for record in weather:
    for city, temps in record.items():
        if temps[2] > max_temp:
            max_temp, max_city = temps[2], city
        if temps[0] < min_temp:
            min_temp, min_city = temps[0], city

print(f"\nCity with Maximum Temp: {max_city} ({max_temp}°C)")
print(f"City with Minimum Temp: {min_city} ({min_temp}°C)")


# 3. Cities with min temp > 30
print("\nCities with Min Temp > 30°C:")
for record in weather:
    for city, temps in record.items():
        if temps[0] > 30:
            print(city)



# 4. Dictionary of average temperatures
avg_temp_dict = {city: temps[1] for record in weather for city, temps in record.items()}
print("\nAverage Temperature Dictionary:")
print(avg_temp_dict)
