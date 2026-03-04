# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial list:", justice_league)

# 1. Calculate number of members
print("1. Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("2. Added new members:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3. Wonder Woman is leader:", justice_league)

# 4. Move Green Lantern in between Aquaman and Flash
# Find Aquaman's position to insert right before him (separating him from Flash)
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index, "Green Lantern")
print("4. Separated Flash and Aquaman:", justice_league)

# 5. New team assembly
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5. New team assembled:", justice_league)

# 6. Sort alphabetically and declare new leader
justice_league.sort()
print("6. Sorted list:", justice_league)
print(f"The new leader is: {justice_league[0]}")  # Prediction: Cyborg is the new leader!
