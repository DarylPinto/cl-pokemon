from random import randint
from time import sleep
from pokemon import Pokemon
from move import Move
from webbrowser import open_new

#Moves
tackle = Move("Tackle", 5, 10, "normal")
thundershock = Move("Thunder Shock", 10, 5, "electric")
ember = Move("Ember", 12, 5, "fire")
razor_leaf = Move("Razor Leaf", 8, 5, "grass")
watergun = Move("Water Gun", 9, 5, "water")
scratch = Move("Scratch", 6, 10, "steel")
bite = Move("Bite", 7, 9, "normal")

#Pokemon
starters = [
	Pokemon("Pikachu", 50, 10, "electric", [tackle, thundershock, scratch]),
	Pokemon("Bulbasaur", 65, 7, "grass", [tackle, razor_leaf, bite]),
	Pokemon("Charmander", 44, 12, "fire", [bite, ember, scratch]),
	Pokemon("Squirtle", 58, 6, "water", [bite, watergun, scratch])
]

#Get int from input
def getIntInRange(prompt, min, max):
	try:
		choice = int(input(prompt))
	except:
		choice = max + 1
	while choice not in range(min, max + 1):
		try:
			choice = int(input("Invalid number. Try again: "))
		except:
			choice = max + 1
	return choice

#Select starter
def select_starter(player):
	print("")
	print("%s, who do you want as your starter?" % (player))
	print("")

	for starter in starters:
		print("%d: %s" % (starters.index(starter) + 1, starter.name))
	print("")

	choice = getIntInRange("%s's starter: " % (player), 1, len(starters)) - 1
	starter = starters.pop(choice)

	print("%s chose %s as their starter!" % (player, starter.name))
	sleep(1)
	return starter

##########
## Game ##
##########
p1 = input("\nTrainer 1, what's your name?\n")
p2 = input("\nAnd what about you, trainer 2?\n")

sleep(0.5)
print("")
print("Nice to meet you two!")
sleep(0.5)

print("Time for the both of you to pick your companions!")

sleep(2)
pokemon1 = select_starter(p1)
pokemon2 = select_starter(p2)
sleep(1)

print("")
print("==============================")
print("Alright, let the battle begin!")
print("==============================")

#start music
open_new("https://www.youtube.com/watch?v=2Jmty_NiaXc")

current_turn = p1

while not pokemon1.has_fainted and not pokemon2.has_fainted:

	def turn(player, pokemon, enemy_pokemon):
		print("\n%s, what will you do?\n" % (player))
		sleep(0.5)
		print("=== %s :: %dHP ===" % (pokemon.name, pokemon.hp))
		for move in pokemon.moves:
			print("%d: %s (%s / %sPP)" % (pokemon.moves.index(move)+1, move.name, move.element, move.pp))
		print("")
		chosen_move_index = getIntInRange("Choose a move to use: ", 1, len(pokemon.moves)) - 1
		pokemon.attack(enemy_pokemon, pokemon.moves[chosen_move_index])

	sleep(1)
	if current_turn == p1:
		turn(p1, pokemon1, pokemon2)
	else:
		turn(p2, pokemon2, pokemon1)

	#change turns
	current_turn = p1 if current_turn == p2 else p2


winner = p1 if pokemon2.has_fainted else p2

print("\nCongratulations, %s! You are the Pokemon master.\n" % (winner))
sleep(2)
print("Thanks for playing!")
input("Press ENTER to exit...")