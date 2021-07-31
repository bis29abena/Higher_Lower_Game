#Higher Vs Lower Game for comparing Instagram celebrities with the highest followers in millions

import random
import art
import game_data
import clear

#Print the game logo

Data = game_data.data


def compare(comp_a, comp_b):

    for dets_dict in comp_a:

        if type(dets_dict) != type(comp_a[dets_dict]):

            followers_A = comp_a[dets_dict]

    print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}")
    print(art.vs)

    for dets_dict in comp_b:

        if type(dets_dict) != type(comp_b[dets_dict]):

            followers_B = comp_b[dets_dict]
    print(f"Compare B: {comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}")

    return followers_A, followers_B


def high_low_game():

    cont = True

    Comp_B = random.choice(Data)

    score = 0

    while cont:

        Comp_A = Comp_B
        Comp_B = random.choice(Data)

        if Comp_A == Comp_B:
            Comp_B = random.choice(Data)

        print(art.logo)


        followers_a, followers_b = compare(Comp_A, Comp_B)

        followers = input("Who has more followers: Type 'A' or 'B': ").upper()

        if followers == 'A' and followers_a > followers_b:
            score+=1

            clear.clear()

            print(F"You are right: your currnt score: {score}")

        elif followers == 'B' and followers_b > followers_a:
            score+=1

            clear.clear()

            print(F"You are right: your currnt score: {score}")
        else:
            clear.clear()

            print(f"Sorry, thats wrong. Final Score {score}")
            
            cont = False



high_low_game()