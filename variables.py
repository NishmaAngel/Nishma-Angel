# 1. Create variable 'pi', assign 22/7, and check its data type
pi = 22/7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))  # Output: <class 'float'>

# 2. Create a variable called 'for' and assign it a value 4
# Uncommenting the line below will result in a SyntaxError.
# for = 4  
# Reason: 'for' is a reserved keyword in Python used to create loops. 
# You cannot use reserved keywords as variable names.

# 3. Simple Interest Calculation
principal = 10000  # P: Principal amount (example value)
rate = 5.5         # R: Rate of interest (example value)
time = 3           # T: Time in years

simple_interest = (principal * rate * time) / 100
print(f"Simple Interest for 3 years is: {simple_interest}")
