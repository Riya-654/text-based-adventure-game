import time
import random
import pygame
pygame.init()

health_up = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/healthup.wav")
low_gold = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/Lowgold.wav")
cards = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/cards.wav")
dice_roll = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/diceroll.wav")
attack_sound = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/attack.wav")
troll_sound = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/trollsound.wav")
background_sound = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/background.wav")
ending_sound = pygame.mixer.Sound("C:/Users/srudr/Downloads/Sounds/ending.wav")
background_sound.set_volume(0.04)

# List of items to be used in the game
shop_items = ["Health Portion          - Worth 50$",
              "Glittering steel armour - Worth 400$",
              "A Talisman              - Worth 300$",
              "Durandal,a mighty sword - Worth 600$",
              "Steel Helmet            - Worth 200$",
              "Go back to village      - None      "]

player_items = ["trusty dagger",
                "Steel armour"]

gift_items = ["Leave"]



inn_info = ["INFO: The cave is nest to stronger enemies",
            "INFO: Go to contest grounds to win gold!",
            "INFO: Buy better weapons in Traven to defeat the troll",]


village_locations = ["Traven",
                     "Inn",
                     "Contest grounds",
                     "Cave"]

contest_items = ["Unknown Key",
                 "Mystery Box key"]

rewards = ["Special Prize1: Unknown Key",
               "Special Prize2: Mystery box key"
               "Deposit 10 Gold, Win back 50 Gold",
               "Deposit Gold and win back Double",]

player_offense_moves = ["You step forward to slash the enemy",
                        "You rise high to deliver a mighty blow",
                        "You deliver an counter attack",
                        "You rain down a series of short swings",
                        "A sharp delivery to penetrate the defense of enemy",
                        "You run around and penetrate the back of the enemy"]

player_defense_moves = ["You hold the sword to counter the enemy attack",
                        "The enemy attacks are repelled by you",
                        "The enemy jumps on you and you roll to the side",
                        "You swing your sword in rythm to the enemy attacks",
                        "You step back away from the enemy",
                        "You dodge the enemy sword and ready to make an attack"
                        ]

enemy_offense_moves = ["The enemy charges at you like a mad bull",
                       "The enemy has a arm streangth of a boulder",
                       "Enemy has wits and great strategy to corner you",
                       "The enemy attacks from behind",
                       "The enemy rolls around and attacks from the side",
                       "The enemy jumps on you",
                       "The enemy fights you head on"]

enemy_defense_moves = ["Enemy has a strong defense",
                       "Your enemy has brains to dodge your attacks",
                       "Your enemy has speed advantage to evade your attacks",
                       "Your enemy has a strength to with stand your attack",
                       "Enemy is determined to take you head on",
                       "Your enemy is a formidable opponent"]

animal_offense_moves = ["The animal charges straight at you ",
                        "The animal attacks you with ferocity ",
                        "The animal attacks you from behind",
                        "The animal tries to bite you",
                        "The animal jumps on you",
                        "The animal uses its claws"]

animal_defense_moves = ["The animal has a thick skin",
                        "The animal has brains to dodge your attacks",
                        "The animal has speed advantage to evade your attacks",
                        "The animal deflects your attacks with claws",
                        "The animal steps back to counter"]

animal_list = ["Boar", "Bear", "Wolf"]

strong_animal_list = ["Leopard", "Tiger", "Werewolf"]

# triggers and declarations to be used in the code
player = ""
shop_count = 0
armour = "available"
durandal = "available"
helmet = "available"
player_health = 100
gold = 500
player_offense_min = 50
player_offense_max = 80
player_defense = 10
contest_day_count = 0
flowers_day_count = 0
forest_explore_count = 0
forest_trigger = "deactivate"
game_over = "deactivate"
troll = "alive"
treasure_box = "not_opened"
chest = "not_opened"
time_zone = "day"
player_status = ""

# function to print messages with a 2 second delay
def print_pause(message):
    print(message)
    time.sleep(2)


# function to print messages with a 1 second delay
def print_pause1(message):
    print(message)
    time.sleep(1)


# function to display the 'items in the list' with a serial number
def list_serial(list):
    for index in range(len(list)):
        print_pause1(str(index+1) + ". " + list[index])
    print_pause1("\n")
    return ""


# function to remove a specific item from a list             
def remove_item(list, item):
    new_list = []
    for index in range(len(list)):
        if list[index] != item:
            new_list.append(list[index])
    list = new_list
    return list


# function to increase player's health within the limit of 100
def health_increase(num):
    global player_health
    if player_health < 100 and player_health > 0:
        pygame.mixer.Sound.play(health_up)
        player_health += num
        if player_health > 100:
            player_health = 100
        return player_health


# function to decrease player's health within the threshold of 0
def health_decrease(health, num):
    if health > 0:
        health += num
        if health < 0:
            health = 0
        return health
    else:
        health = 0
        return health


# function to display a message whenever the gold is insufficient
def low_gold_message():
    global gold
    global player
    pygame.mixer.Sound.play(low_gold)
    print_pause("NOTE: You do not have enough cash " + player + "!")
    print_pause("Your Gold : " + gold)
    print_pause("NOTE: Try earning some in the town contest")


# ------------main function to trigger the game-------------
def adventure_game():
    global player
    # input to ask for the player's name
    pygame.mixer.Sound.play(background_sound,-1)
    player = input("\nWhat is your name?\n")
    print_pause("\nOn guard " + player + "!")
    print_pause("This is a royal quest to find the hidden treasure!")
    print_pause("your status: gold=500"
                              "\n\t     health=100")
    print_pause("your weapons: trusty dagger"
                               "\n\t      steel armour")
    village()


# A branch sequence to the function 'adventure_game'
def village():
    # trigger to end the game from the function 'fight_sequence'
    if game_over == "activate":
        print_pause("\n\nGame over. Try again ........")
        exit()
    # village intro
    # player's choice
    print_pause("\nwelcome to the fabled village of Yorkshire")
    print_pause("Where would you like to venture:")
    # displays list of village locations in a serial list
    village_choice = input(list_serial(village_locations)).lower()
    # if player decides to enter into the traven
    if "1" in village_choice:
        print_pause("\nYou have entered Traven to make business")
        shop()
    # if player decides to enter into the Inn
    elif "2" in village_choice:
        print_pause("\nYou have checked into an Inn")
        inn()
    # if player decides to enter into the contest grounds
    elif "3" in village_choice:
        print_pause("\nYou head towards the contest grounds with curiosity")
        contest_grounds()
    # if player decides to enter into the cave
    elif "4" in village_choice:
        print_pause("You step into the darkness of cave courageously !!")
        print_pause("The cave is a labyrinth of multiple partitions")
        cave()
    # if player decides to enter into the forest
    elif "5" in village_choice:
        forest()
    
    

# funtion to trigger shop sequence in the game
def shop():
    global gold
    global shop_items
    global player_items
    global player
    global player_status
    global player_offense_min
    global player_offense_max
    global player_defense
    global player_health     
    global armour
    global durandal
    global helmet
    global gift_items
    global shop_count
    shop_count += 1
    # An introduction to be used only one time in the game
    if shop_count == 1:
        print_pause("SHOPKEEPER: Haah.. a fine warrior.")
        print_pause("SHOPKEEPER: Welcome to the Traven of trade and purchase.")
        print_pause("SHOPKEEPER: We have a large collection from far lands "
                    "of Euthopia.")
        print_pause("SHOPKEEPER: Best and most rarest of all, if you can "
                    "afford that is!")
        print_pause("SHOPKEEPER: Feel free to browse through them.")
    # A message to be displayed only if the player is wanted
    elif player_status == "wanted":
        print_pause("SHOPKEEPER: I am not allowed to trade with "
                    "criminals " + player + ".")
        print_pause("SHOPKEEPER: But I am willing to keep this as a "
                    "secret between us")
    # A message to be used throughout the game, if player revisit the shop
    else:
        print_pause("\nSHOPKEEPER: Welcome back " + player + " !!")
        print_pause("SHOPKEEPER: Back for more?")
        print_pause("SHOPKEEPER: Let me see if I can find, what you need.")

    print_pause("SHOPKEEPER: What do you want to purchase? Name it.")
    # Displays shops items in a serial list and take desired input from player
    shop_choice = input(list_serial(shop_items)).lower()
    # if player wants to buy health potion in the shop
    if "1" in shop_choice:
        if gold >= 50 and player_health < 100:
            print_pause("SHOPKEEPER: One must stock up on health or face "
                        "certain death")
            print_pause("Gold: " + str(gold) + ", - 50")
            gold -= 50
            print_pause("Your Gold: " + str(gold))
            health_increase(25)
            print_pause("Your health increased +25, feel stronger now ?")
            print_pause("Your Health: " + str(player_health))
        elif player_health == 100:
            print_pause("SHOPKEEPER: You already have full health")
        elif gold < 50:
            low_gold_message()
    
    elif "2" in shop_choice and armour == "available":
        if gold >= 400:
            print_pause("SHOPKEEPER: Shiny shiny, makes enemies whiny tiny")
            print_pause("Note: Now you have 'Steel Armour' in your possession")
            shop_items = remove_item(shop_items,
                                     "Glittering steel armour - Worth 400$")
            player_items.append("Glittering steel armour")
            gift_items.append("Glittering steel armour")
            armour = "not available"
            print_pause("Gold: " + str(gold) + ", - 400")
            gold -= 400
            print_pause("Your Gold: " + str(gold))
        else:
            low_gold_message()
    # if player wants to buy 'talisman' in the shop
    elif "3" in shop_choice:
        if gold >= 300:
            print_pause("SHOPKEEPER: I see you are in serious "
                        "business " + player)
            print_pause("SHOPKEEPER: Good luck. You are gonna need it.")
            print_pause("Note: You have the talisman, "
                        "it adds fire element to weapons")
            shop_items = remove_item(shop_items,
                                     "A Talisman              - Worth 300$")
            player_items.append("Talisman")
            print_pause("Gold: " + str(gold) + ", - 300")
            gold -= 300
            print_pause("Your Gold: " + str(gold))
        else:
            low_gold_message()
   
    # if player wants to buy 'durandal' in the shop                 ***
    # by adding / durandal == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "4" in shop_choice and durandal == "available":
        if gold >= 600 and "Excaliber" not in player_items:
            print_pause("SHOPKEEPER: A great sword for the true warrior")
            print_pause("SHOPKEEPER: It is said to bring out the inner "
                        "strenth of the warrior from the depths of volcano")
            print_pause("NOTE: You now possess the 'Durandal', a mighty sword")
            player_offense_min = 20
            player_offense_max = 50
            print_pause("NOTE: Your offense has increased "
                        "to: " + str(player_offense_max))
            print_pause("NOTE: You are stronger now and")
            print_pause("      ready to fight stronger enemies.")
            shop_items = remove_item(shop_items,
                                     "Durandal,a mighty sword - Worth 600$")
            player_items.append("Durandal")
            durandal = "not available"
            print_pause("Gold: " + str(gold) + ", - 600")
            gold -= 600
            print_pause("Your Gold: " + str(gold))
        elif "Excaliber" in player_items:
            print_pause("SHOPKEEPER: You already possess a more "
                        "powerful sword")
            print_pause("SHOPKEEPER: These is no need to buy this sword")
        elif gold < 600:
            low_gold_message()
    
            
    # if player wants to buy 'steel helmet' in the shop
    # by adding / helmet == "available" / in the below statement-
    # player cannot buy this item, if the item is already sold out
    elif "5" in shop_choice and helmet == "available":
        if gold >= 200:
            print_pause("SHOPKEEPER: Good choice, better safe than sorry.")
            print_pause("NOTE: You have accquired a 'Steel Helmet'")
            shop_items = remove_item(shop_items,
                                     "Steel Helmet            - Worth 200$")
            player_items.append("Steel Helmet")
            helmet = "not available"
            print_pause("Gold: " + str(gold) + ", - 200")
            gold -= 200
            print_pause("Your Gold: " + str(gold) + "\n")
            print_pause("NOTE: Your defense has been increased")
            print_pause("Defense :" + str(player_defense) + ", + 10")
            player_defense += 10
            print_pause("Player Defense increased to: " + str(player_defense))
        elif gold < 200:
            low_gold_message()
    # if player wants to get back to the village
    elif "6" in shop_choice:
        print_pause("You head back to the village")
        village()
    # if player gives an unrecognized input
    else:
        print_pause("SHOPKEEPER: I don't understand, "
                    "Specify the number of the item clearly")
        shop()
    # After trading, player has to get back to the village
    print_pause("\nYou took care of the business in Traven, as of now "
                "and head back to the village")
    village()


# a function to run 'inn' sequence
def inn():
    print_pause("This is a place to rest & refresh your body and soul")
    inner_inn()


# A branch sequence to the funtion 'inn'
def inner_inn():
    # player's choice
    print_pause("\nWhat would you like to do:")
    inn_choice = input("1)get information from inn owner"
                       "\n2) Rent a Room"
                       "\n3)Go back to Village\n").lower()
    #if player chooses to talk to inn owner
    if "1" in inn_choice:
        print_pause("INN OWNER:i have one for you")
        print_pause(random.choice(inn_info))
        print_pause("INN OWNER: That's all you get for now!")
        inner_inn()



    # if player chooses to enter the room
    if "2" in inn_choice:
        room()
    # if player chooses to enter the village
    elif "3" in inn_choice:
        village()
    # condition to deal with unrecognized input
    else:
        print_pause("Enter a valid choice: Room? or village?")
        inner_inn()


# A branch sequence to the funtion 'inner_inn'       **
def room():               
    global gold
    print_pause("\nYou enterd the room all tired and deprived of sleep")
    print_pause("You were charged 20 gold for the room")
    print_pause("Gold: " + str(gold) + ", -20")
    gold -= 20
    print_pause("Your Gold: " + str(gold))


# function to trigger the location 'contest grounds' in the village
def contest_grounds():
    global contest_day_count
    
    # if player visits 'contest grounds' during daytime
    if time_zone == "day":
        contest_day_count += 1
        # intro to be used only once in the game
        if contest_day_count == 1:
            print_pause("surprisingly, this country holds contests "
                        "in gambling")
            print_pause("People of this country prefers peace over violence")
        # if player visits more than once
        if contest_day_count >= 1:
            print_pause("Would you like to take part in the gambling?")
            contest_choice_day = input("1. Yes"
                                       "\n2. No\n").lower()
            if "1" in contest_choice_day:
                game_day()
            elif "2" in contest_choice_day:
                print_pause("HOST: Farewell, stranger.")
                print_pause("HOST: Do come back another time")
                village()
            # condition to handle unrecognized inputs from the player
            else:
                print_pause("HOST: Make up your mind stranger. 'yes' "
                            "or 'no' ?")
                contest_grounds()
    
# A branch sequence to the funtion 'contest_grounds'
def game_day():
    global gold
    global contest_items
    global rewards
    global contest_items
    global player_items
    global player_status
    # a trigger if the player is wanted
   # if player_status == "wanted":
      #print_pause("Leave stranger, you are gonna get me in trouble")
        #print_pause("You are forced to leave the contest grounds")
        #print_pause("You head back to the village")
        #village()
    # choice to play different games
    print_pause("\nHOST: welcome stranger, what would you like to play?")
    pygame.mixer.Sound.play(cards)
    contest_day_choice = input("1) Evens & Odds"
                               "\n2) Double or nothing"
                               "\n3) View rewards\n").lower()
    # if player choose 'evens & odds' game
    if "1" in contest_day_choice:
        if gold >= 10:
            print_pause("HOST: Deposit 10 gold to play the game")
            print_pause("Your Gold: " + str(gold) + " , -10")
            gold -= 10
            print_pause("Your Gold: " + str(gold))
            value1, value2 = roll_dice()
            if (value1+value2) % 2 == 0:
                value = "even"
            else:
                value = "odd"

            print_pause(str(value1) + "+" + str(value2) + " "
                        "= " + str(value1 + value2) + ", " + value)

            if value == "even":
                print_pause("HOST: Evens it is... Congratulations stranger")
                print_pause("HOST: You have won 50 gold")
                print_pause("Your Gold: " + str(gold) + " , +50")
                gold += 50
                print_pause("Your Gold: " + str(gold))
                if "Mystery Box key" in contest_items:
                    print_pause("Also I have a special prize waiting to be won.")
                    print_pause("Note: You have received an 'Mystery Box Key'.")
                    contest_items = remove_item(contest_items, "Mystery Box Key")
                    player_items.append("Mystery Box key")
                    rewards = remove_item(rewards,
                                              "Special Prize2: Mystery Box Key ")
                
            else:
                print_pause("HOST: Odds are against you stranger.., "
                            "you lost your deposit")
        # if player does not have enough gold
        else:
            low_gold_message()
            village()
    # if player choose 'double or nothing' game
    elif "2" in contest_day_choice:
        print_pause("\nHOST: Deposit gold as you desire")
        print_pause("HOST: If both dices are evens or odd , you win")
        print_pause("HOST: If you win , you will have double the deposit")
        print_pause("HOST: Lose, I keep the gold.")
        # if player has not win the special prize already
        if "Unknown Key" in contest_items:
            print_pause("Also I have a special prize waiting to be won.")
        # take a desired amount of bet from the player's input
        gold_deposited = int(input("How much would you like to bet:"))
        print_pause("Your Gold: " + str(gold) + " , - " + str(gold_deposited))
        gold -= gold_deposited
        if gold >= 0:
            print_pause("Your Gold= " + str(gold))
            value1, value2 = roll_dice()
            print_pause("Dices : " + str(value1) + "," + str(value2))
            # if player wins
            if (value1 % 2) == (value2 % 2):
                # if player has not win the special prize already
                if "Unknown Key" in contest_items:
                    print_pause("HOST: Marvelous stranger!, it's your"
                                " lucky day")
                    print_pause("HOST: I have just the rare item as the prize")
                    print_pause("Note: You have received an 'Unknown Key'.")
                    contest_items = remove_item(contest_items, "Unknown Key")
                    player_items.append("Unknown Key")
                    rewards = remove_item(rewards,
                                              "Special Prize1: Unknown Key")
                    print_pause("Host: I'll keep the deposit just this once")
                    print_pause("HOST: consider it an even trade for the "
                                "rare item")
                # if player has already won the special prize
                else:
                    print_pause("HOST: Congratulation, stranger! you won "
                                "this game")
                    gold_deposited = 2*gold_deposited
                    print_pause("Your Gold: " + str(gold) + " , "
                                "+ " + str(gold_deposited))
                    gold += gold_deposited
                    print_pause("Your Gold: " + str(gold))
            # if player loses
            else:
                print_pause("Host: It is not as easy as it sounds stranger!!")
                print_pause("HOST: I get to keep the gold")
        # if player does not have enough gold
        else:
            low_gold_message()
            gold += gold_deposited
            print_pause("Your Gold= " + str(gold))
            village()
    # if player wants to check the rewards before playing the game
    elif "3" in contest_day_choice:
        print_pause(list_serial(rewards))
        game_day()
    # condition to deal unrecognized input
    else:
        print_pause("HOST: Say the correct words stranger")
        game_day()
    # choice to play the game again
    print_pause("\nHOST: would you like to play again stranger ?")
    play_again = input("1)yes\n2)no\n").lower()
    if "1" in play_again:
        game_day()
    # if player wants to leave the contest grounds
    else:
        print_pause("HOST: Good bye, stranger")
        village()


# A branch sequence to the funtion 'game_day'
def roll_dice():
    print_pause("\nRolling Dice:")
    pygame.mixer.Sound.play(dice_roll)
    value1 = random.randint(1, 6)
    print_pause("Dice 1: " + str(value1))
    value2 = random.randint(1, 6)
    print_pause("Dice 2: " + str(value2))
    # returns a random number from each dice
    return value1, value2


# A branch sequence to the funtion 'game_night_contest'
def fight_sequence(enemy, enemy_offense_min, enemy_offense_max, enemy_defense):
    global player_health
    global player_offense_min
    global player_offense_max
    global player_defense
    global player_offense_moves
    global player_defense_moves
    global enemy_offense_moves
    global enemy_defense_moves
    global animal_offense_moves
    global animal_defense_moves
    global rewards_night
    global animal_list
    global strong_animal_list
    global game_over

    enemy_health = 100
    # a loop to let player and enemy deal random damage in each turn
    for turn in range(40):
        # if trun is even number and player is alive
        if turn % 2 == 0 and player_health > 0:
            print_pause("Player Attacks....//")
            pygame.mixer.Sound.play(attack_sound)
            # print random message from the list 'player_offense_moves'
            print_pause(random.choice(player_offense_moves))
            # if enemy is an animal
            if enemy in animal_list or enemy in strong_animal_list:
                # print random message from the list 'animal_defense_moves'
                print_pause(random.choice(animal_defense_moves))
            # if enemy is not an animal
            else:
                # print random message from the list 'enemy_defense_moves'
                print_pause(random.choice(enemy_defense_moves))
            # assign random number with in the range to player's offence
            player_offense = random.randint(player_offense_min,
                                            player_offense_max)
            enemy_damage = enemy_defense - player_offense
            # as damage decreases the health, it cannot be a positive number
            if enemy_damage > 0:
                enemy_damage = 0
            print_pause("Enemy damage : " + str(enemy_damage))
            # decrement enemy health based on damage
            enemy_health = health_decrease(enemy_health, enemy_damage)
            # display both player's and enemy's health
            print_pause("Player_health: " + str(player_health))
            print_pause("Enemy_health : " + str(enemy_health) + "\n")
        # if trun is odd number and enemy is alive
        elif turn % 2 == 1 and enemy_health > 0:
            print_pause(enemy + " Attacks....//")
            # if enemy is an animal
            if enemy in animal_list or enemy in strong_animal_list:
                # print random message from the list 'animal_offense_moves'
                print_pause(random.choice(animal_offense_moves))
            # if enemy is not an animal
            else:
                # print random message from the list 'enemy_offense_moves'
                print_pause(random.choice(enemy_offense_moves))
            # print random message from the list 'player_defense_moves'
            print_pause(random.choice(player_defense_moves))
            # assign random number with in the range to enemy's offence
            enemy_offense = random.randint(enemy_offense_min,
                                           enemy_offense_max)
            player_damage = player_defense - enemy_offense
            # as damage decreases the health, it cannot be a positive number
            if player_damage > 0:
                player_damage = 0
            print_pause("Player damage: " + str(player_damage))
            # decrement player's health based on damage
            player_health = health_decrease(player_health, player_damage)
            # display both player's and enemy's health
            print_pause("Player_health: " + str(player_health))
            print_pause("Enemy_health : " + str(enemy_health) + "\n")
        # if enemy loses the battle
        if player_health > 0 and enemy_health <= 0:
            print_pause("You have successfully slain the " + enemy)
            print_pause("You emerge victorious !!")
            return "player wins"
        # if player loses the battle
        elif player_health <= 0 and enemy_health > 0:
            print_pause("You lost this battle....")
            # if the fight is in the contest grounds
            # your health will be restored to bare minimum
            if enemy == "warrior" or enemy == "gladiator":
                print_pause("NOTE: Your health restored to 10")
                print_pause("NOTE: Find a way to increase your health")
                player_health = 10
                print_pause("Your Health: " + str(player_health) + "\n")
                return "enemy wins"
            # if the fight is not in the contest grounds
            # game ends
            print_pause("You are dead.")
            game_over = "activate"
            village()

# funtion to trigger the location 'cave' in the village
def cave():
    global troll
    global player_items
    global gold
    global treasure_box
    global chest
    global monster
    # if the player have fire element to enter the cave
    if "Talisman" not in player_items:
        print_pause("You need the talisman to explore the dark cave")
        print_pause("You head back to the village")
        village()
    print_pause("Enter the number of the route you want to take.")
    cave_choice = input("\n1 Dungeon1"
                        "\n2 Dungeon2"
                        "\n3 Back to village\n")
    # if player wants to enter route 1
    if cave_choice == "1":
        # if troll guarding the route 1 is alive
        if troll == "alive":
            pygame.mixer.Sound.play(troll_sound)
            print_pause("This route is guarded by a troll")
            print_pause("Troll is a strong opponent with thick skin")
            print_pause("what would you do?")
            route1_choice = input("\n1 Fight"
                                  "\n2 Run away\n").lower()
            # if player chooses to fight the troll
            if "1" in route1_choice:
                print_pause("You decided to fight the troll\n")
                fight_result = fight_sequence("Troll", 20, 40, 10)
                if fight_result == "player wins":
                    print_pause("You have triumphed over the troll")
                    # trigger to skip this part if visited again
                    troll = "defeated"
                    
            # if player chooses to run
            elif "2" in route1_choice:
                print_pause("You have strategically with drawn from a "
                            "death battle")
                print_pause("You should head back to the village to "
                            "prepare for the battle, before trying again")
                cave()
            # condition to deal with unrecognized input
            
        # if the troll has been already slain
        else:
            print_pause("The troll guarding the route has been slain")
            print_pause("You can travel furthur deep into the route now")
        # After the troll part
        print_pause("\nYou travel deep into the Route 1\n")
        print_pause("There is a Treasure box at the center of the room")
        print_pause("Would you like to open the Treasure box?")
        treasure_box = input("\n1) Yes"
                             "\n2) No\n").lower()
        # if player chooses to open the box
        if "1" in treasure_box:
            # if the treasure has been already looted
            if treasure_box == "empty":
                print_pause("The Treasure Box is already looted by you")
                print_pause("There is nothing intersting here")
                print_pause("You head back to the cave entrance\n")
                cave()

            elif "Mystery Box key" in player_items:
                 print_pause("Would you like to try the 'Mystery Box Key', "
                        "you have won in the contest grounds?")
                 route1_choice = input("\n1) Yes"
                                  "\n2) No\n").lower()
                 if "1" in route1_choice:
                    print_pause("You open the box and you find gold inside!")
                    print_pause("Your gold: "+str(gold)+"+2000")
                    gold += 2000
                    print_pause("Your gold:"+ str(gold))
                    cave()

            # if the player does not have the key
            else:
                print_pause("Win the mystery box key in contest grounds and return")
                print_pause("You head back to the cave entrance\n")
                cave()
        # if player chooses not to open the box/ gives unrecognized input
        else:
            print_pause("You head back to the cave entrance\n")
            cave()

    # if player wants to enter route 2                 **
    elif cave_choice == "2":
        print_pause("NOTE: The entrance to the cave is locked and "
                    "requires a key to open")
        # if player has the key, won in the contest grounds
        if "Unknown Key" in player_items:
            print_pause("Would you like to try the 'Unknown Key', "
                        "you have won in the contest grounds?")
            route2_choice = input("\n1) Yes"
                                  "\n2) No\n").lower()
            # if player tries to open the door using unknown key
            if "1" in route2_choice:
                print_pause("The key matches the lock")
                print_pause("You opened the door and head furthur deep "
                            "into Route2")
                print_pause("In the room you found a chest eating dust")
                print_pause("The chest looks old and dangerous")
                print_pause("What would you do ?")
                chest_choice = input("\n1) Open"
                                     "\n2) Head back\n")
                # if player wants to open the chest
                if "1" in chest_choice:
                    
                    # if the chest is not looted
                    print_pause("You reluctantly open the chest")
                    print_pause("Voila...!! Its a treasure chest "
                                "filled with gold....")
                    print_pause("You have found the hidden treasure!")
                    credits()
                # if player do not want to open chest/gives unrecognized input
                else:
                    print_pause("You head back to the cave entrance\n")
                    cave()
            # if player do not want to open door/gives unrecognized input
            else:
                print_pause("You head back to the cave entrance\n")
                cave()
        # if player does not have the key, won in the contest grounds
        else:
            print_pause("NOTE: Come back after you acccquired "
                        "the key to 'Route2'in contest grounds")
            print_pause("You head back to the cave entrance\n")
            cave()
    

    # if player choose to head back to the village
    elif cave_choice == "3":
        print_pause("You head back to the village\n")
        village()
    # condition to deal with unrecognized input
    else:
        print_pause("\nEnter a valid number")
        cave()

# function to be displayed if player successfully complete the game
def credits():
    global player
    print_pause("\n\n         //  Congratulations on completing the game  //")
    exit()

# ------------ Game Trigger ------------
adventure_game()
