import os
from game_data import data
import random
from art import vs


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

score = 0

def celebrity_one():
    number = random.randint(0,51)
    # pega um numero aleatorio e seleciona esse elemento no dicionario

    first_celebrity_selector = data[number]
    celebrity_one_name = first_celebrity_selector["name"]
    celebrity_one_follow_count = first_celebrity_selector["follower_count"]
    celebrity_one_description = first_celebrity_selector["description"]
    celebrity_one_country = first_celebrity_selector["country"]

    print(f"Compare A: {celebrity_one_name}, a {celebrity_one_description} from {celebrity_one_country}")

    return celebrity_one_follow_count #da o valor de seguidores da primeira celebridade

def celebrity_two():
    number = random.randint(0, 51)
    second_celebrity_selector = data[number]
    celebrity_two_name = second_celebrity_selector["name"]
    celebrity_two_follow_count = second_celebrity_selector["follower_count"]
    celebrity_two_description = second_celebrity_selector["description"]
    celebrity_two_country = second_celebrity_selector["country"]

    print(f"Against B: {celebrity_two_name}, a {celebrity_two_description} from {celebrity_two_country}")

    return celebrity_two_follow_count #da o valor de seguidores da segunda celebridade

def check_right(celebrity_a_followers, celebrity_b_followers,score,choice):
    if choice == "a" and celebrity_a_followers > celebrity_b_followers:
        clear_console()
        score += 1
        print(f"You right! Current score: {score}")
        return score

    elif choice == "b" and celebrity_a_followers < celebrity_b_followers:
        clear_console()
        score += 1
        print(f"You right! Current score: {score}")
        return score
    else:
        clear_console()
        print(f"Sorry, that's wrong. Final score:  {score}")
        exit()




while True:

    clear_console()


    celebrity_a_followers = celebrity_one()
    print(vs)
    celebrity_b_followers = celebrity_two()



    choice = input("Who was more followers? Type 'A' or 'B': ").lower()
    score = check_right(celebrity_a_followers, celebrity_b_followers, score, choice)



