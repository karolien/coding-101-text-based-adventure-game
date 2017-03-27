print("Welcome to Choose Your Own Adventure")
name = input("Please enter a character name: ") #introduce variables
print("Hi, " + name + " thank you for playing.")
print("Please enter your choice for race: \n0. Elf\n1. Goblin\n2. Dwarf\n3. Human")
race_choice = int(input("Enter your choice: "))
races = ["Elf", "Goblin", "Dwarf", "Human"]
race = races[race_choice]
print("You chose " + race)
