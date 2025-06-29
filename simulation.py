import random
import os
# a model is a mathematical representation of a thing or a process. 

#Player 1
def player_1_offensive_power(player_1_height, player_1_feeling):
    player_1_3_point_skill = random.randint((50 + player_1_feeling),(100 + player_1_feeling))
    player_1_field_goal_skill = random.randint((50 + player_1_feeling),(100 + player_1_feeling + player_1_height))
    player_1_speed = random.randint((50 - player_1_height + player_1_feeling),(100 + player_1_feeling))
    return (player_1_speed + player_1_field_goal_skill + player_1_3_point_skill)
    

def player_1_defensive_power(player_1_height, player_1_feeling):  
    player_1_defense = random.randint((50 + player_1_feeling),(100 + player_1_feeling))
    player_1_rebounds = random.randint((50 + (player_1_height * 3)),(100 + (player_1_height * 3)))
    player_1_steals = random.randint((50 - player_1_height),(100 - player_1_height))
    return (player_1_defense + player_1_steals + player_1_rebounds)



#Player 2
def player_2_offensive_power(player_2_height, player_2_feeling):
    player_2_3_point_skill = random.randint((50 + player_2_feeling),(100 + player_2_feeling))
    player_2_field_goal_skill = random.randint((50 + player_2_feeling),(100 + player_2_feeling + player_2_height))
    player_2_speed = random.randint((50 - player_2_height + player_2_feeling),(100 + player_2_feeling))
    return (player_2_speed + player_2_field_goal_skill + player_2_3_point_skill)
    

def player_2_defensive_power(player_2_height, player_2_feeling):   
    player_2_defense = random.randint((50 + player_2_feeling),(100 + player_2_feeling))
    player_2_rebounds = random.randint((50 + (player_2_height * 3)),(100 + (player_2_height * 3)))
    player_2_steals = random.randint((50 - player_2_height),(100 - player_2_height))
    return (player_2_defense + player_2_steals + player_2_rebounds)


player_1_name = "Lebron James"
player_1_height = 7
player_1_morale = 3
player_1_feeling = random.randint(1,5)


player_2_name = "James Harden"
player_2_height = 4
player_2_morale = 2
player_2_feeling = random.randint(1,5)


game_score_player_1 = 0
game_score_player_2 = 0 

desiredscore = int(input("what do you want these people to play to?: "))

while game_score_player_1 < desiredscore and game_score_player_2 < desiredscore:
        if player_2_offensive_power(player_2_height,player_2_feeling) > player_1_defensive_power(player_2_height, player_2_feeling):
            game_score_player_2 = game_score_player_2 + 1
            print(player_2_name, "scored! Score is: ", game_score_player_1, ":", game_score_player_2)
        if player_1_offensive_power(player_2_height, player_2_feeling) > player_2_defensive_power(player_2_height,player_2_feeling):
            game_score_player_1 = game_score_player_1 + 1
            print(player_1_name, "scored! Score is: ", game_score_player_1, ":", game_score_player_2)
        if game_score_player_1 > 10:
            (player_1_defensive_power(player_1_height, player_1_feeling) * player_1_morale)
            (player_1_offensive_power(player_1_height, player_1_feeling) * player_1_morale)
        if game_score_player_2 > 10:
            (player_2_defensive_power(player_2_height, player_2_feeling) * player_2_morale)
            (player_2_offensive_power(player_2_height, player_2_feeling) * player_2_morale)

if game_score_player_1 > game_score_player_2:
    print(player_1_name, "WON!!")
else:
    print(player_2_name, "WON!!")