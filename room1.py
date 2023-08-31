import time

digits_list = []       #first number in room 3(7)

def congrats():
	print("Congratulations you made it to the next room! Do you have what it takes to go to the next room?")

def restart():
	answer_restart = input("Would you like to start again?(Y/N)")
	if answer_restart == 'Y' or 'y':
		room_three()
	elif answer_restart == 'N' or 'n':
		print_pause("Well this is awkward.... What now?")

def print_pause(message):
    print(message)
    time.sleep(2)

def room_one():       #room one code

	print("INTRODUCTION TO THE ROOM")    #give introduction to the room
	answer1 = input("Would you like to look around the room? (Y/N)")

	if answer1 == 'Y' or 'y':

		print_pause("You start looking around the room....\nYou see a scenery so you go ahead and inspect it further.")
		print("You find a key on the scenery you take it and unlock the door!\nYou proceed to the next room!")

	elif answer1 == 'N' or 'n':
		print_pause("Well... what now?")

def room_three():
	congrats()
	print("INTRODUCTION TO THE ROOM")     #give introduction to the room
	answer3 = input("Would you like to look around the room? (Y/N)")
	if answer3 == 'Y' or 'y':
		print_pause("You start looking around the room....\nOn the wall you see the number 7 written with red colour")
		answer4 = input("Would you like to note down the number?")
		if answer4 == 'Y' or 'y':
			print("You note down the number")
			digits_list.append(7)
		elif answer4 == 'N' or 'n':
			pass

		print_pause("You continue looking around the room....You see a few objects kept which you can use.\nThere is a vase labelled 2.6 kg\nThere is a rock labelled 1.5kg\nThere is a statue labelled 3.9 kg")
		answer_vase = input("Would you like to place the vase on the weight balance?(Y/N)")
		if answer_vase == 'Y' or 'y':
			print("You placed the vase")
			print_pause("The screen under the weight balance now displays 1500g")
		elif answer_vase == 'N' or 'n':
			pass
		answer_rock = input("Would you like to place the vase on the weight balance?(Y/N)")
		if answer_rock == 'Y' or 'y':
			print("You placed the rock")
			print_pause("....BINGO! The door unlocked\nYou proceed to the next room.")
		elif answer_rock == 'N' or 'n':
			pass
		answer_statue = input("Would you like to place the statue on the weight balance?(Y/N)")
		if answer_statue == 'Y' or 'y':
			print("You placed the statue")
			print_pause(".... The weight balance now tilted on one side\nThe door did not unlock!")
			print("YOU LOST!")
			restart()
			
		elif answer_statue == 'N' or 'n':
			print_pause("....There are no more objects left")
			print("YOU LOST!")
			restart()
	elif answer3 == 'N' or 'n':
		print_pause("Well... what now?")


room_one()
room_three()

