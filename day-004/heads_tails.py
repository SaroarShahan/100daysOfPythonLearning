import random

def heads_tails():
    coin = random.randint(0, 1)

    if coin == 0:
        print("Heads")
    else:
        print("Tails")

heads_tails()