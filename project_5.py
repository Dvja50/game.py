
import time, random, os, sys

room_items_dictionary = {"1": "Red Key", "2": "Green Key", "3": "Blue Key"}

inventory_list = []
item_list = ["Red Key", "Green Key","Blue Key"]

player_hp = 10
player_ap = 4
enemies_list = ["Red Clown", "Ghost Clown","Big Nose Clown","Screaming Clown", "Wacky Clown","Laughing Clown","Crazy Eye Clown"]
enemies_list_dictionary = {"1": "Ghost Clown", "2": "Big Nose Clown", "3": "Red Clown"}

def main():
    choice = play_game()
    while True:
        if choice == "1":
            choice = enter_porch()
        elif choice == "2":
            choice = enter_entryway()
        elif choice == "3":
            choice = enter_kitchen()
        elif choice == "4":
            choice = enter_diningroom()
        elif choice == "5":
            choice = enter_livingroom()
        else:
            break
    print("Thank you for playing!\nGAME OVER!")



def play_game():
    print("""
    Welcome to the Clown House! >:)
    You can move N (north), S (south), E (east), or W (west) by
    typing the upper or lower case letter.
    Type 'E' to end the program.
    Type 'S' to start the game!""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["S", "Q"]:
            break
        else:
            print("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == "S":
        return "1"
    else:
        return "Q"
    
def print_room_header(room):
    line = '-' * 25
    print(f"\n{line}{room}{line}")
##Function##
def check_inventory():
    if set(inventory_list) == set(item_list):
        print("\n\nYOU WON! You've found all the items!")
        os._exit(0)

def enter_porch():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Porch")
    print("""
    You are on the porch of the old "Clown House"
    You notice that the windows are broken. 
    It's a dark and stormy night.
    Will you go in?\n
    Your options:
    Press 'N' to enter the house
    Press 'Q' to quit the game\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>>  ').upper()
    if option == 'S':
        if "1" in room_items_dictionary: ##Use this
            print("Searching room...")
            time.sleep(2)
            #if random.randint(1, 3) == 1:
            item = room_items_dictionary.get("1")
            print(f"You found a {item}")
            inventory_list.append(item)
            del room_items_dictionary["1"]
            check_inventory()
        else:
            print("You didn't find any items")
    else:
        print("No items in room")
    while True:
        choice = input("Enter your choice: N or Q\n>> ").upper()
        if choice in ["N","Q"]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice == "N":
        return "2"
    else:
        return "Q"
    
def enter_entryway():
    global room_items_dictionary, items_list, inventory_list
    print_room_header("Entryway")
    print("""
    You are in the entryway of the house. It is colorful with loud music.
    You realize you are NOT the only one here.
    There is a passageway to the N and another to the E.
    The porch is behind you to the S.\n""")
    if "1" in enemies_list_dictionary:  
        print("There is an enemy in this room")
        fight_enemy()
    option = input('Select "L" to leave or "S" to search the room.\n>>  ').upper()
    if option == 'S':
        if "2" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            item = room_items_dictionary.get("2")
            print(f"You found a {item}")
            inventory_list.append(item)
            del room_items_dictionary["2"]
            check_inventory()
        else:
            print("You didn't find any items")
    else:
        print("No items in room")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "N", "S", "E"]:
            if choice == "N":
                print("The door is locked...")
                time.sleep(2)
                if "Green Key" in inventory_list:
                    print("You use the key to unlock the door")
                    time.sleep(2)
                    break
                else:
                    print("You can't open the door")
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "3"
    elif choice == "S":
        return "1"
    elif choice == "E":
        return "5"
    else:
        return "Q"
def enter_kitchen():
    print_room_header("Kitchen")
    print("""
    You are in the kitchen.
    You see pies sitting on each counter, and pools of blood.
    You hear a squeaky noise in the corner of the room.
    You can go to the S or to the E.\n""")
    if "2" in enemies_list_dictionary:  
        print("There is a CLOWN in here")
        fight_enemy()
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "S","E"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "2"
    elif choice == "E":
        return "4"
    else:
        return "Q"
    
def enter_diningroom():
    print_room_header("Dining Room")
    print("""
    You are in the dining room.
    There are red chairs, cob webs, and dust all over the room.
    There are remains of a meal on the table.
    You hear a scream
    Was that scream coming from the west?
    You can go S or W.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "S", "W"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "5"
    elif choice == "W":
        return "3"
    else:
        return "Q"
    

def enter_livingroom():
    print_room_header("Living Room")
    print("""
    You are in the living room. You sense there is something lurking...
          Suddenly, you realize that there is...
    You can go N or W.\n""")
    
    if "3" in enemies_list_dictionary:  
        print("There is a CLOWN in this room!")
        fight_enemy()
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == 'S':
        if "3" in room_items_dictionary:
            print("Searching the room...")
            time.sleep(2)
            item = room_items_dictionary.get("3")
            print(f"You found a {item}!")
            inventory_list.append(item)
            del room_items_dictionary["3"]  
            check_inventory()  
        else:
            print("You didn't find anything.")
    else:
        print("The room is empty. Nothing to find here.")

    while True:
        choice = input("Which direction do you want to go? (N, W, Q to quit)\n>> ").upper()
        if choice in ["Q", "N", "W"]:
            break
        else:
            print("Invalid direction! You can't go that way.\n")
    
    if choice == "N":
        return "4"
    elif choice == "W":
        return "2"
    else:
        return "Q"

def fight_enemy():
    global player_hp, player_ap, enemies_list
    enemy = random.choice(enemies_list) 
    enemies_list.remove(enemy) 
    enemy_hp = random.randint(5, 10)
    enemy_ap = random.randint(1, 5)
    
    print(f"A {enemy} attacks you!")
    while True:
        choice = input('Enter "F" to fight or "R" to run away\n>> ').upper()
        if choice == "F":
            break
        elif choice == "R":
            print("You bravely run away!\n")
            return 
        else:
            print("Not a valid choice\n")
    while True:
        player_attack = int(random.random() * player_ap)
        enemy_attack = int(random.random() * enemy_ap)
        time.sleep(1)
        if player_attack > enemy_attack:
            print(f"You attack the {enemy}!\n")
            enemy_hp = enemy_hp - player_attack
            print(f"{enemy} suffered {player_attack} damage: {enemy}'s health is now at {enemy_hp}\n")
        elif enemy_attack > player_attack:
            print(f"The {enemy} attacks you!\n")
            player_hp = player_hp - enemy_attack
            print(f"You suffered {enemy_attack} damage: Your health is now at {player_hp}\n")
        else:
            print(f"You struggle with the {enemy}!\n")
        time.sleep(1)    
        if player_hp < 1:
            print("You have been killed!")
            print("GAME OVER")
            sys.exit()
        if enemy_hp < 1:
            print(f"The {enemy} has been killed!")
            return

main()

