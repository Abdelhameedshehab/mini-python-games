gravities = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15
}

planets = list(gravities.keys())

print("Pick up the planet (enter number):")
for i, planet in enumerate(planets, start=1):
    print(f"{i}. {planet}")

choice = input("Your choice: ")

try:
    choice_num = int(choice)
    if 1 <= choice_num <= len(planets):
        plant = planets[choice_num - 1]
    else:
        print("❌ Wrong answer! Number out of range.")
        exit()
except ValueError:
    print("❌ Invalid input! Please enter a number only.")
    exit()

weight_input = input("Enter your weight on Earth: ")

try:
    object_weight = float(weight_input)
    earth_gravity = gravities["Earth"]
    mass = object_weight / earth_gravity
    new_weight = mass * gravities[plant]
    print("You would weigh " + str(round(new_weight)) + " kg on " + plant + ".")
except ValueError:
    print("❌ Invalid input! Please enter numbers only.")
    exit()
