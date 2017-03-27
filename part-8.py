import time

print("Welcome to Choose Your Own Adventure")
name = input("Please enter a character name: ") #introduce variables
print("Hi, " + name + " thank you for playing.")
print("Please enter your choice for race: \n0. Elf\n1. Goblin\n2. Dwarf\n3. Human")
race_choice = int(input("Enter your choice: "))
races = ["Elf", "Goblin", "Dwarf", "Human"]
race = races[race_choice]
print("You chose " + race)
time.sleep(2)
if race == "Elf":
    print("Your homeland is in the forest")
elif race == "Goblin":
    print("Your homeland is underground")
elif race == "Dwarf":
    print("Your homeland is in the mines underground")
else:
    print("Your homeland is in the city")
time.sleep(3)
print("A wild monster appears! Select a reponse:\n0. Cower in fear!\n1. RUN!\n2. Fight!")
response = int(input("Enter your choice: "))
if response == 0:
    print("You were eaten by the monster!")
    quit()
elif response == 1:
    print("You run from the scene and the monster goes and destroys a village.")
else:
    print("You prepare for battle")
    for i in range(3):
        time.sleep(2)
        print("Do you want to hit the monster high or low?\n0. High\n1. Low")
        response = int(input("Your choice: ")) #illustrates overwriting variables
        if response == 0:
            print("You hit high, the monster takes some damage.")
        elif response == 1:
            print("You hit low, the monster takes some damage.")
    time.sleep(2)
    print("You killed the monster!")
