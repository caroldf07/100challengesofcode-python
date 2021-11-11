# 1. Create a greeting for your program.
print("Hello there!")
# 2. Ask the user for the city that they grew up in.
city = input("Please, write your hometown's name: \n")
# 3. Ask the user for the name of a pet.
pet = input("Please, write your first pet's name: \n")
# 4. Combine the name of their city and pet and show them their band name.
band_name = (city + " " + pet)
# 5. Make sure the input cursor shows on a new line
print(f"Your band name is: %s" % band_name)
