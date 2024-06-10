# grading exercise

#heads and tails - two-up

""" tasks - import random 
        make random toss
        get player to add to bank
        get bet from player
        determine who will win
        add or subtract from bank
        play again?
"""

import random
possible =['Heads', 'Tails']
shorter=['h','t']

def toss():
    coin1=random.choice(possible)
    coin2=random.choice(possible)
    return coin1, coin2

def user_bet():
    answer=''
    while True:
        answer=input('Choose your outcome - "H" for Heads or "T" for Tails. : ').lower()
        if answer in shorter:
            choice=answer
            break
        else:
            print("Try again")
    return choice

print(user_bet())

# toss()

def bank():
    bank_balance=0
    while bank_balance == 0:
        add_bank_balance=int(input("How much do you want to add to the bank?  Input a value :$"))
        bank_balance +=add_bank_balance
    print(f"Your bank balance is ${bank_balance}.")
    return bank_balance

bank()
# print(f"Your bank balance is ${bank()}")