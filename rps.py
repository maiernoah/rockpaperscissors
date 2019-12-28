import time
import random
tie = " "
tie_score = 0
compy_score = 0

print(
    "\nWelcome to Rock, Paper, Scissors. \nYour time is better spent doing other things. \nShame on you. Go ride a "
    "bike. Get outside. Make your mother proud.")
print("\n")
time.sleep(2)



def game():
    insultList = ["use red solo cups for thanksgiving dinner.",
                  "licked a frozen lightpole to see what would happen.",
                  "thought the Trojan war was about a condom shortage.",
                  "don\'t know the difference between Degas and Degrassi.",
                  "burned your tongue on coffee you knew was hot.",
                  "ate frozen peas without thawing them.",
                  "have a hampster for a mother.",
                  "smell like elderberries.",
                  "don\'t know how to change a flat tire.",
                  "still have a crush on Malibu Barbie.",
                  "eat your fingernails.",
                  "ate dry cereal this morning because your milk was spoiled.",
                  "kissed your cousin because you wanted more practice."]

    global tie

    tie = False
    victory_list = ['Bad move. I chose ',
                    'I knew you\'d pick that. I picked',
                    'Ha! I picked',
                    'Dumb move. I picked']
    victory = random.choice(victory_list)
    user_choice = str.upper(input('Ok fine, let\'s play. Choose rock, paper, or scissors: '))

    if random.randint(0, 100) < 40:
        print("")
        print("I choose you...", user_choice)
        print("\nTies only count in horseshoes and hand grenades")
        print("")
        global tie_score
        global compy_score
        tie_score = tie_score + 1
        tie = True
        print("")
        print("Your Score: 0 " + "Ties:", tie_score,"My Score: ",compy_score)
        print("")
        play_again = str.upper(input("Want to play again? (Y/N): "))
        while play_again == "Y":
            game()
        print("Thanks for playing, you scruffy looking nerf herder.")
        quit()
    elif user_choice == "ROCK":
        print("")
        global compy_choice
        compy_score = compy_score + 1
        compy_choice = "PAPER"
        print("\n", victory, compy_choice)
        print("")
        print("You lose, I win. I can make trillions of calculations each second. You", random.choice(insultList))
        print("")
        print("Your Score: 0 " + "Ties:", tie_score, "My Score: ", compy_score)
        print("")
        play_again = str.upper(input("Want to play again? (Y/N): "))
        while play_again == "Y":
            game()
        print("Thanks for playing, you scruffy looking nerf herder.")
        quit()
    if user_choice == "PAPER":
        print("")
        compy_score = compy_score + 1
        compy_choice = "SCISSORS"
        print("\n", victory, compy_choice)
        print("")
        print("You lose, I win. I can make trillions of calculations each second. You", random.choice(insultList))
        print("")
        print("Your Score: 0 " + "Ties:", tie_score, "My Score: ", compy_score)
        print("")
        play_again = str.upper(input("Want to play again? (Y/N): "))
        while play_again == "Y":
            game()
        print("Thanks for playing, you scruffy looking nerf herder.")
        quit()
    if user_choice == "SCISSORS":
        print("")
        compy_score = compy_score + 1
        compy_choice = "ROCK"
        print("\n", victory, compy_choice)
        print("")
        print("You lose, I win. I can make trillions of calculations each second. You", random.choice(insultList))
        print("")
        print("Your Score: 0 " + "Ties:", tie_score, "My Score: ", compy_score)
        print("")
        play_again = str.upper(input("Want to play again? (Y/N): "))
        while play_again == "Y":
            game()
        print("Thanks for playing, you scruffy looking nerf herder.")
        quit()

    if user_choice != "ROCK" and user_choice != "PAPER":
        if user_choice != "SCISSORS":
            print("ERROR: You spelled it wrong bozo.")
            game()

game()
play_again = str.upper(input("Want to play again? (Y/N): "))
while play_again == "Y":
    game()
print("Thanks for playing, you scruffy looking nerf herder.")

