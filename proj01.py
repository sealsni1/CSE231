# Take input from user
rod_val = (input("Input rods: "))

# float the users input value
rod_val = float(rod_val)

# display the float value to the user
print("\nYour value is", rod_val,
      "rods.\n")

print('Conversions')

# Calculations

# 5.0292 meters = 1 rod
meters = float(rod_val * 5.0292)
print('Meters:', round(meters, 3))

# 0.3048 meters = 1 foot
feet = float(meters * (1/.3048))
print('Feet:', round(feet, 3))

# 1609.34 meters = 1 mile
miles = float(meters / 1609.34)
print('Miles:', round(miles, 3))

# 40 rods = 1 furlong
furlongs = float(rod_val / 40)
print("Furlongs:", round(furlongs, 3))

# 3.1 miles = 60 minutes
minutes = float(miles * (60.0/3.1))
print('Minutes to walk', rod_val, 'rods:', round(minutes, 3))
