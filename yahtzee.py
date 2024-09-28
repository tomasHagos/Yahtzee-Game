import random
def rolldice():
    dice_list = []
    for _ in range(5):
        dice_list.append(random.randint(1,6))
    print("Here are your rolls:")
    print(dice_list)
    #reroll one
    reroll_strings = input("Which one would you want to re-roll ex (999)?")
    #removing the dices
    for characters in reroll_strings:
        if characters.isdigit() and (dice_list.count(int(characters)) != 0):
            dice_list.remove(int(characters)) #changing the characters to an integer
    #adding the new rolled die
    for _ in range(5 - len(dice_list)):
        dice_list.append(random.randint(1,6))
    print("Here are your dice after rerolls:")
    print(dice_list)
    print("you get one more reroll:")
    reroll_strings = input("Type the numbers of the dice you want to reroll (ex 566):")
    #remove the dice the user wants to reroll
    for character in reroll_strings:
        if character.isdigit() and (dice_list.count(int(character)) != 0):
            dice_list.remove(int(character)) #note the integer conversion because the list contains integeres

            #add new rerolls
            for _ in range(5 - len(dice_list)):
                dice_list.append(random.randint(1,6))
            print("Here are your dice after reroll:")
            #print(dice_list)

            return dice_list





    return (dice_list)
# defining function for present options
def present_options(score_list):
    SelectedScore = "100"
    while SelectedScore != "x":
        print(f"""Choose your scoring selection
          A -{score_list[0]}-Ones (add only the ones)
          B -{score_list[1]}- Twos (add only the twos)
          C -{score_list[2]}- Threes (add only the twos)
          D -{score_list[3]}-Fours (add only the twos)
          E -{score_list[4]}- Fives (add only the twos)
          F -{score_list[5]}-Sixes (add only the twos)
          G -{score_list[6]}- Three of a kind (total up all dice)
          H -{score_list[7]}- Four of a kind (total up all dice)
          I -{score_list[8]}- Full House (25 points)
          J -{score_list[9]}-Small Straight (30 points)
          K -{score_list[10]}- Large Straight (40 points)
          L -{score_list[11]}-Yahtzee (50 points)
          M -{score_list[12]}-Chance (total up all dice)""")
        response = input("Type the letter of your selection: ")
        response = response.upper()[0] #this will get the first
        score_index = ord(response) - 65
        SelectedScore = score_list[score_index]
        if 0 <= score_index <= 12:
            selectedScore = score_list[score_index]
    return response.upper()


def score_ones(dice_list):
        player_score = dice_list.count(1)
        return player_score
def score_twos(dice_list):
     score = dice_list.count(2)
     return score * 2


def score_threes(dice_list):
     score = dice_list.count(3)
     return score * 3
def score_fours(dice_list):
    score = dice_list.count(4)
    return score * 4
def score_fives(dice_list):
    score = dice_list.count(5)
    return score * 5
def score_sixes(dice_list):
    score = dice_list.count(6)
    return score * 6

def Three_kind(dice_list):
    for x in dice_list:
      count = dice_list.count(x)
      if count >= 3:
        return sum(dice_list)
      else:
        return 0

def four_kind(dice_list):
    for item in dice_list:
        count = dice_list.count(item)
        if count >= 4:
            return sum(dice_list)
        else:
            return 0
def full_house(dice_list):
  for i in dice_list:
    count = dice_list.count(i)
    if count == 3:
      #removing the first number
      dice_list.remove(i)
      #removing the second number
      dice_list.remove(i)
      #removing the third number
      dice_list.remove(i)
      for x in dice_list:
        new_count = dice_list.count(x)
        if new_count == 2:
          return 25
        else:
          return 0
    elif count == 2:
      dice_list.remove(i)
      dice_list.remove(i)
      for item in dice_list:
        count = dice_list.count(item)
        if count == 3:
          return 25
        else:
          return 0
    else:
      return 0



def small_straight(dice_list):
        dice_list.sort()
        streak = 1
        longest_streak = 1
        for i in range(1, 5):
            if dice_list[i] == dice_list[i - 1] + 1:
                streak += 1
            elif dice_list[i] == dice_list[i - 1]:
                pass
            else:
                streak = 1
            if streak > longest_streak:
                longest_streak = streak
            if longest_streak >= 4:
                return 30
        else:
            return 0

def large_straight(dice_list):
    dice_list.sort()
    streak = 1
    longest_streak = 1
    for i in range(1,5):
        if dice_list[i] == dice_list[i - 1] + 1:
            streak += 1
        elif dice_list[i] == dice_list[i - 1]:
            pass
        else:
            streak = 1
        if streak > longest_streak:
            longest_streak = streak
        if longest_streak >= 5:
            return 40
    else:
        return 0


def yahtzee(dice_list):
    for item in dice_list:
        count = dice_list.count(item)
        if count == 5:
            return 50
        else:
            return 0

def chance(dice_list):
    score = sum(dice_list)
    return score
def getScore():
    player1_score = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    player2_score = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    player1 = 0
    player2 = 0
    game = True
    while game:
            player1_turn = True
            if player1 == 13:
                player1_turn = False
            if player2 == 13:
                player2_turn = False
            player1 += 1
            while player1_turn:
                print("Player 1")
                player_dice = rolldice()
                print(player_dice)
                player_selection = present_options(player1_score)
                if player_selection == "A":
                    score = score_ones(player_dice)
                    player1_score[0] = score
                elif player_selection == "B":
                    score = score_twos(player_dice)
                    player1_score[1] = score
                elif player_selection == "C":
                    score = score_threes(player_dice)
                    player1_score[2] = score
                elif player_selection == "D":
                    score = score_fours(player_dice)
                    player1_score[3] = score
                elif player_selection == "E":
                    score = score_fives(player_dice)
                    player1_score[4] = score
                elif player_selection == "F":
                    score = score_sixes(player_dice)
                    player1_score[5] = score
                elif player_selection == "G":
                    score = Three_kind(player_dice)
                    player1_score[6] = score
                elif player_selection == "H":
                    score = four_kind(player_dice)
                    player1_score[7] = score
                elif player_selection == "I":
                    score = full_house(player_dice)
                    player1_score[8] = score
                elif player_selection == "J":
                    score = small_straight(player_dice)
                    player1_score[9] = score
                elif player_selection == "K":
                    score = large_straight(player_dice)
                    player1_score[10] = score
                elif player_selection == "L":
                    score = yahtzee(player_dice)
                    player1_score[11] = score
                elif player_selection == "M":
                    score = chance(player_dice)
                    player1_score[12] = score
                else:
                    print("option not recognized")
                player1_turn = False
                print(f" You scored {score}")
                player2_turn = True
            while player2_turn:
                    player2 += 1
                    print("Player 2")
                    player_dice = rolldice()
                    print(player_dice)
                    player_selection = present_options(player2_score)
                    if player_selection == "A":
                        score = score_ones(player_dice)
                        player2_score[0] = score
                    elif player_selection == "B":
                        score = score_twos(player_dice)
                        player2_score[1] = score
                    elif player_selection == "C":
                        score = score_threes(player_dice)
                        player2_score[2] = score
                    elif player_selection == "D":
                        score = score_fours(player_dice)
                        player2_score[3] = score
                    elif player_selection == "E":
                        score = score_fives(player_dice)
                        player2_score[4] = score
                    elif player_selection == "F":
                        score = score_sixes(player_dice)
                        player2_score[5] = score
                    elif player_selection == "G":
                        score = Three_kind(player_dice)
                        player2_score[6] = score
                    elif player_selection == "H":
                        score = four_kind(player_dice)
                        player2_score[7] = score
                    elif player_selection == "I":
                        score = full_house(player_dice)
                        player2_score[8] = score
                    elif player_selection == "J":
                        score = small_straight(player_dice)
                        player2_score[9] = score
                    elif player_selection == "K":
                        score = large_straight(player_dice)
                        player2_score[10] = score
                    elif player_selection == "L":
                        score = yahtzee(player_dice)
                        player2_score[11] = score
                    elif player_selection == "M":
                        score = chance(player_dice)
                        player2_score[12] = score
                    else:
                        print("option not recognized")
                    player2_turn = False
                    print(f" You scored {score}")
            total1 = sum(player1_score)
            total2 = sum(player2_score)
            if total1 > total2:
                print("Player 1 is the winner")
            elif total1 < total2:
                print("Player 2 is the winner")
            else:
                print("It's  a tie")
getScore()
play_again = input("Do you want to play again(yes/no)?")
while play_again == "yes":
    getScore()
    play_again = input("Do you want to play again(yes/no)?")
