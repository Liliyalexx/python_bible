# ask user for their name
name = input("what is your name?: ")

# ask user for the age
age = input("what is your age?: ")
            

# ask user what they enjoy
enjoy = input("what you enjoy about!: ")

# ask user for city
city = input ("what city are you from?: ")

# create output text
string = " Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, city, enjoy)

# print output to screen
print(output)
