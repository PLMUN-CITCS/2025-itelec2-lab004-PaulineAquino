# Your Name
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Input Handling, Data Type Conversion, and String Formatting in Python

# Get integer input from the user
user_integer = int(input("Enter an integer: "))

# Get decimal (float) input from the user
user_decimal = float(input("Enter a decimal number: "))

# Get string input from the user
user_text = input("Enter a string: ")

#Display formatted output using old-style formatting
print("Formatted Output using old-style formatting:") 
print("Integer: %d" % user_integer) 
print("Decimal: %.2f" % user_decimal)  # Format decimal to two places 
print("String: %s" % user_text)

# Display formatted output using f-strings
print("Formatted Output using f-strings:") 
print(f"Integer: {user_integer}") 
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to two places 
print(f"String: {user_text}")
