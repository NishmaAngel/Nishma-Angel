# 1. BMI Calculator
print("--- BMI Calculator ---")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Output: Obesity")
elif bmi >= 25:
    print("Output: Overweight")
elif bmi >= 18.5:
    print("Output: Normal")
else:
    print("Output: Underweight")

# Definition of cities and countries (For parts 2 & 3)
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# 2. Determine country from city
city_input = input("\nEnter a city name (for country check): ")

if city_input in australia:
    print(f"{city_input} is in Australia")
elif city_input in uae:
    print(f"{city_input} is in UAE")
elif city_input in india:
    print(f"{city_input} is in India")
else:
    print("City not found in our database.")

# 3. Check if two cities belong to the same country
city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in india and city2 in india:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
