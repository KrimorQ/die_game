import random, sys
dies = 3
die_sides = random.randint(1,7)
in_game = True
player_total = 0
player_win = 0
enemy_total = 0
enemy_win = 0
print("welcome to my die game")

while in_game:
    print(f"Game mode: You both have {dies} die(s) with sides of {die_sides}")
    print("Press (r) to roll\nPress (s) for settings\nPress (q) to quit")
    player_move = input(">")
    if player_move == "s":
        print("Here you can change the game settings")
        print(f"Amount of die(s): {dies}\nDie sides: {die_sides}")
        dies = int(input("Amount of die(s): "))
        die_sides = int(input("Amount of sides: "))

    if player_move == "q":
        sys.exit()
        print("Thanks for playing")
        print(f"The score was\nPLAYER: {player_win}\nENEMY: {enemy_win}")
    if player_move == "r":
        for i in range(dies):
            number = random.randint(1,6)
            print(number)
            player_total += number

        for i in range(dies):
            number = random.randint(1,6)
            print(number)
            enemy_total += number


        if player_total > enemy_total:
            print(f"ENEMY: {enemy_total}\nPLAYER: {player_total}")
            print("PLAYER WINS")
            player_win += 1
            if player_win >= 3:
                print(f"You won!\nPLAYER: {player_win}\nENEMY: {enemy_win}")
            enemy_total = 0
            player_total = 0
        elif enemy_total > player_total:
            print(f"ENEMY: {enemy_total}\nPLAYER: {player_total}")
            print("ENEMY WINS")
            if enemy_win >= 3:
                print(f"You lost!\nPLAYER: {player_win}\nENEMY: {enemy_win}")
            enemy_win += 1
            enemy_total = 0
            player_total = 0
        else:
            print(f"ENEMY: {enemy_total}\nPLAYER: {player_total}")
            print("DRAW")
            enemy_total = 0
            player_total = 0
