# Task-1

Anton_age = 21

# Calculating other ages based on the riddle

Beth_age = Anton_age + 6
Chen_age = Beth_age + 20
Drew_age = Chen_age + Anton_age
Ethan_age = Chen_age

# Printing the names and ages

print("Anton is", Anton_age, "years old.")
print("Beth is", Beth_age, "years old.")
print("Chen is", Chen_age, "years old.")
print("Drew is", Drew_age, "years old.")
print("Ethan is", Ethan_age, "years old.")


# Task-2

name:str= "Alice"
age = 30
city:str = "New York"

# Constructing the sentence using f-strings
sentence = f"{name} is {age} years old and lives in {city}."

# Printing the sentence
print(sentence)


#Task#3

# 1.Capitalize the first letter

s = "hElLo WoRlD"
capitalized = s.capitalize()  # "Hello world"
print(capitalized)

# 2.Convert to uppercase
s = "hElLo WoRlD"
uppercase = s.upper()  # "HELLO WORLD"
print(uppercase)

# 3.Convert to lowercase)
s = "hElLo WoRlD"
lowercase = s.lower()  # "hello world"
print(lowercase)


#Task-4

s = "the quick brown fox jumps over the lazy dog"

# Index of "fox"

index_of_fox = s.find("fox")
print(f"Index of 'fox' is {index_of_fox}")

# Count of "the"

count_of_the = s.count("the")
print(f"'the' appears {count_of_the} times")


#Task#5


s = "I love programming in Python"
s_replaced = s.replace("Python", "Java")
print(s_replaced)


#Task#6


s = "apple,banana,cherry,dates"

# Split the string into a list of substrings based on the delimiter ','
s_split = s.split(',')

# Join the list of substrings back into a single string, with each element separated by a space
s_joined = ' '.join(s_split)

print(s_joined)



#Task#7


s = "   Python is fun!  "

# Remove leading and trailing whitespace characters
s_trimmed = s.strip()

# Left justify the string within a field of width 20, using '*' as the fill character
s_left_justified = s_trimmed.ljust(20, '*')

# Right justify the string within a field of width 20, using '*' as the fill character
s_right_justified = s_trimmed.rjust(20, '*')

print("Trimmed:", s_trimmed)
print("Left Justified:", s_left_justified)
print("Right Justified:", s_right_justified)

#Task#8


num = 45

# Obtain the binary representation of num

binary_representation = bin(num)

# Print the binary representation (excluding the '0b' prefix)
print(binary_representation)


#Task#9


base = 3
exponent = 4

# Compute base raised to the power of exponent
result = base ** exponent

print(result)



#Task#10

value = 12.34567

# Round value to the nearest integer
rounded_integer = round(value)

# Round value to two decimal places
rounded_two_decimals = round(value, 2)

print("Rounded to nearest integer:", rounded_integer)
print("Rounded to two decimal places:", rounded_two_decimals)



#End

