# Dragon Realm
# A game by Aaron Hobson
# 10/7/2017

# import stuff
import random
import time

# Show Introduction
def show_intro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on site.''')
    print()


def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave

def check_cave(cave_chosen):
    global score
    print("You approach the cave slowly...")
    time.sleep(2)
    print("Smells like dragon farts...")
    time.sleep(2)
    print("A big ol' DRAGON jumps out in front of you and opens its jaws and...")
    print()
    time.sleep(2)

    friendly_dragon = random.randint(1, 2)

    if cave_chosen == str(friendly_dragon):
        print("gives you his treasure!")
        score += 1
    else:
        print("he eats you whole and you spend days in agony digested in his stomach!")
        if score >= 1:
            score -= 1
        
def play():
    still_playing = True
    while still_playing:
        show_intro()
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to continue,, q to quit)")
        choice = input()
        if choice == "q":
            still_playing = False
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playing!")


play()








        


