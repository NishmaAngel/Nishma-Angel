# 1. Format function formatting
def format_number(num, formatting):
    return format(num, formatting)

result = format_number(145, 'o')
print(f"Formatted result: {result}") 
# Representation: The 'o' format specifier converts the decimal number into its Octal (base-8) representation.

# 2. Pond Area and Water calculation
pi_value = 3.14
radius = 84

# Calculate Area
circle_area = pi_value * (radius ** 2)
print(f"Area of the pond: {circle_area} square meters")

# Bonus: Calculate water amount (without decimal)
water_per_sq_meter = 1.4
total_water = circle_area * water_per_sq_meter
print(f"Total amount of water in the pond: {int(total_water)} liters")

# 3. Speed Calculation
distance_meters = 490
time_minutes = 7
time_seconds = time_minutes * 60  # convert minutes to seconds

speed_mps = distance_meters / time_seconds
print(f"Speed: {int(speed_mps)} meters per second")
