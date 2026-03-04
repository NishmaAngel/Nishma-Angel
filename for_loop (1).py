import random

# Part 1: Dice Rolling Simulation
rolls_count_6 = 0
rolls_count_1 = 0
double_6_count = 0
previous_roll = 0

print("--- Rolling the die 20 times ---")
# Roll the die 20 times
for _ in range(20):
    current_roll = random.randint(1, 6)
    
    if current_roll == 6:
        rolls_count_6 += 1
        # Check for two 6s in a row
        if previous_roll == 6:
            double_6_count += 1
    elif current_roll == 1:
        rolls_count_1 += 1
        
    previous_roll = current_roll

print(f"Times rolled a 6: {rolls_count_6}")
print(f"Times rolled a 1: {rolls_count_1}")
print(f"Times rolled two 6s in a row: {double_6_count}")


# Part 2: Jumping Jacks Workout Simulation
total_jumping_jacks = 100
set_size = 10
completed_jacks = 0

print("\n--- Starting the Jumping Jack Workout! ---")

for i in range(total_jumping_jacks // set_size):
    completed_jacks += set_size
    
    # If 100 reached, congratulate and stop.
    if completed_jacks == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
        
    print(f"\nYou just did {set_size} jumping jacks.")
    tired_reply = input("Are you tired? ").strip().lower()
    
    if tired_reply in ["yes", "y"]:
        skip_reply = input("Do you want to skip the remaining sets? ").strip().lower()
        if skip_reply in ["yes", "y"]:
            print(f"You completed a total of {completed_jacks} jumping jacks.")
            break 
    else: # Rejects yes, assumes no/n
        remaining_jacks = total_jumping_jacks - completed_jacks
        print(f"{remaining_jacks} jumping jacks are remaining.")
