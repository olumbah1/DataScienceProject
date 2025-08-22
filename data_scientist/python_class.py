# Example: positive indexing
my_string = "Hello, World!"

# Accessing characters using positive indexing
first_char = my_string[0]
second_char = my_string[1]
last_char = my_string[12]

print("Positive indexing:")
print("First character:", first_char)
print("Second character:", second_char)
print("Last character:", last_char)

# Accessing characters using negative indexing
last_char_negative = my_string[-1]
second_last_char = my_string[-2]
first_char_negative = my_string[-13]

print("\nNegative indexing:")
print("Last character:", last_char_negative)
print("Second last character:", second_last_char)
print("First character:", first_char_negative)


# Immutable strings


original_string = "Hello"
new_string = original_string + ", World!"

# Print the new variable
print('\n',new_string)

# Example: newline (\n)
print("Hello,\nWorld!")

# Example: tab (\t)
print("Name:\tJohn\nAge:\t25")

# Example: backslash (\\)
print("This is a backslash: \\")

# Example: single quote (\')
print('He said, \'Hello!\'')

# Example: double quote (\")
print("She exclaimed, \"Wow!\"")

# Example: carriage return (\r)
print("Overwrite\rThis text.")

# Example: backspace (\b)
print("Remove\b This")

# Example: alert (\a)
print("This is an alert!\a")

# Example: octal representation (\ooo)
print("Octal representation: \110")

# Example: hexadecimal representation (\xhh)
print("Hexadecimal representation: \x48")



string1 = "Programming"
string2 = " is fun!"

print(string1 + string2)



name = "John"
age = 30

print('Name:\t', name)
print('Age:\t', age)

print("He said,'Hello!'")

# Example: slicing – positive indexing
text = "Python is amazing"
substring = text[0:6]
print(substring)

# Example: slicing – negative indexing 1
text = "Python is amazing"
substring = text[-7:-1]
print(substring)

# Example: slicing – negative indexing 2

text = "Python is amazing"
substring = text[-7:]
print(substring)

# Built in Strings

# 1. upper()
# The upper() method transforms all characters in a string to uppercase.

# Example: upper() method

original_string = "hello, world!"
uppercase_string = original_string.upper()
print(uppercase_string)

# 2. lower()
# The lower() method converts all characters in a string to lowercase.

# Example: lower() method

original_string = "Hello, World!"
lowercase_string = original_string.lower()
print(lowercase_string)

# 3. capitalize()¶
# The capitalize() method capitalises the first character of a string.

# Example: capitalize() method

original_string = "hello, world!"
capitalised_string = original_string.capitalize()
print(capitalised_string)

# Example: title() method
original_string = 'hello!, world'
capitalised_every_first_string = original_string.title()
print(capitalised_every_first_string)

# 4. strip()
# The strip() method is used to remove leading and trailing whitespaces from a string. This is particularly useful when dealing with user inputs or processing data from external sources.

# Example: strip() method

raw_input = "    This is a sentence with spaces.    "
trimmed_input = raw_input.strip()
print(trimmed_input)

# Example: replace() method

original_text = "Python is a powerful programming language."
modified_text = original_text.replace("Python", "JavaScript")
print(modified_text)

# 6. find()¶
# The find() method is employed to locate the index of a substring within a string. It returns the index of the first occurrence of the specified substring or -1 if the substring is not found.


sentence = "Searching for a keyword in this sentence."
index = sentence.find("keyword")
print(index)

# string concatenate
greeting = "Hey"
name = "Alice"
punctuation = "!"

personalised_greeting = greeting+ " " + name + punctuation

print(personalised_greeting)

# Replication

pattern = "ABC"

repeated_pattern = pattern * 10

print(repeated_pattern)

# 
pattern = "ABC"

repeated_pattern = " " .join([pattern] * 10)

print(repeated_pattern)


# Convert the entire string to uppercase.
manipulation_string = "python string manipulation"

uppercase_modified = manipulation_string.upper()

print(uppercase_modified)

# Capitalise the first letter of the string.
manipulation_string = "python string manipulation"
capitalize_string = manipulation_string.capitalize()
print(capitalize_string)

# Replace the word "string" with "text."
manipulation_string = "python string manipulation"
replaced_string = manipulation_string.replace("string", "text")
print(replaced_string)


complex_string = "apple pie, apple juice, apple tart"

replaced_complex = complex_string.replace("apple", "orange")

print(replaced_complex)


# Exercises
# Perform operations
num1 = 15
num2 = 7

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = float(num1) / num2

# Print the variables
print("Sum: ", sum_result)
print("Difference: ", difference_result)
print("Product: ", product_result)
print("Division: ", division_result)

# Variable creation
first_name = "Jane"
last_name = "Doe"

# String manipulation and concatenation
full_name = first_name + " " + last_name

# Display result in uppercase
print("Full name in uppercase:", full_name.upper())

num_of_books = "15"

# Casting to integer
books_read = int(num_of_books)

# Calculate average books read per week
weeks_in_month = 4
average_books_per_week = books_read / weeks_in_month

# Print result
print("You have read an average of " + str(average_books_per_week) + " books per week.")


# Given information
name = "John Doe"
age = 25
height = 1.75  # in metres
weight = 68.5  # in kilograms

# Calculate BMI
bmi = weight / (height ** 2)

# Print result
print((name) + "'s BMI is: "+ str(bmi))

# Given the variables
product_name = "Widget XYZ"
initial_quantity = 100
price_per_unit = 12.50
discount_percentage = 0.15

# Calculate total value of initial stock
total_value = initial_quantity * price_per_unit

# Apply discount and calculate discounted price
discounted_value = total_value - (total_value * discount_percentage)

# Update quantity based on new shipment
new_shipment = 30
updated_quantity = initial_quantity + new_shipment

# Display results
print("=" * 40)
print("\n----------- Stocks Details ------------")
print("Product name:", product_name)
print("Initial quantity:", initial_quantity)
print("Price per unit: $", price_per_unit)
print("Discount percentage:", discount_percentage * 100, "%")

print("\n-------------- Results ----------------")
print("Total value of initial stock: $", total_value)
print("Discounted value: $", discounted_value)
print("Updated quantity in stock:", updated_quantity)
print("=" * 40)