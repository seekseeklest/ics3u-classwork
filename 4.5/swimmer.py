import time

swimmer1 = "GALLANT"
swimmer2 = "GOOFUS "

minimum_temperature = 79.0  # degrees Fahrenheit
current_temperature = 0.0
saved_temperature = 0.0
swim_time = 0

current_temperature = float(input("What is the current water temperature? "))
saved_temperature = current_temperature  # saves a copy of this value so we can get it back later.

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer1} approaches the lake....")

swim_time = 0
while current_temperature >= minimum_temperature:
    print(f"\t{swimmer1} swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)  # pauses for 600 milliseconds
    current_temperature -= 0.5  # subtracts 1/2 a degree from the water temperature
    print(f"\tThe current water temperature is now {current_temperature} F.")

print(f"{swimmer1} stops swimming. Total swim time: {swim_time} min.")

current_temperature = saved_temperature  # restores original water temperature

print(f"\nOkay, so the current water temperature is {current_temperature} F.")
print(f"{swimmer2} approaches the lake....")

swim_time = 0
while True:
    print("\t" + swimmer2 + " swims for a bit.", end="")
    swim_time += 1
    print(f" Swim time: {swim_time} min.")
    time.sleep(0.6)
    current_temperature -= 0.5
    print(f"\tThe current water temperature is now {current_temperature} F.")
    
    if current_temperature < minimum_temperature:
        break

print(f"{swimmer2} stops swimming. Total swim time: {swim_time} min.")

# 1. Do Goofus and Gallant swim for the same amount of time if you input 80.5 as the current water temperature?
# Answer: No, they do not swim for the same amount of time. Gallant stops swimming when the temperature drops below 79°F,
# but Goofus swims even when it drops below that point, due to his loop continuing until 'break'.

# 2. Run the program with a starting temperature of 78. What changes?
# Answer: Gallant doesn't swim at all because the starting temperature is below 79°F.
# Goofus swims once, even though the temperature is below 79°F.

# 3. Does Gallant check the water temperature first, or does he just dive right in?
# Answer: Gallant checks the water temperature first before swimming. He doesn't swim if it's too cold.

# 4. Does Goofus check the water temperature first or just dive in?
# Answer: Goofus doesn't check the temperature first. He just dives right in and only stops when the water gets too cold.

# 5. What is the difference between the first while loop and the second while loop? What does the 'break' keyword do?
# Answer: The first while loop checks the temperature before Gallant swims, so he doesn't swim if it's too cold.
# The second while loop (Goofus) always runs at least once, and 'break' stops the loop when the temperature drops below 79°F.

# 6. Which loop is a pre-test loop and which is a post-test loop?
# Answer: Gallant's loop is a pre-test loop because it checks the condition before swimming.
# Goofus's loop is a post-test loop because it runs at least once and then checks the condition.

