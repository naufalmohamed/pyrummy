import random
from itertools import islice

dic = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13",

"H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13",

"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13",

"S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13"]

def assign(dic):

    player_dic = random.sample(dic, 13)

    left_over = []

    common_set = []

    for i in dic:
        if i in player_dic:
            pass
        else:
            left_over.append(i)

    computer_dic = random.sample(left_over,13)

    for i in dic:
        if i in player_dic or i in computer_dic:
            pass
        else:
            common_set.append(i)

    return common_set, player_dic, computer_dic


def set_sort_strip(lis):

    lis.sort()

    club = []
    heart = []
    spade = []
    diamond = []

    for i in lis:
        if i[0] == "C":
            x = i.replace("C","")
            club.append(int(x))

        elif i[0] == "H":
            x = i.replace("H","")
            heart.append(int(x))

        elif i[0] == "S":
            x = i.replace("S","")
            spade.append(int(x))

        elif i[0] == "D":
            x = i.replace("D","")
            diamond.append(int(x))

        else:
            pass

    club.sort()
    diamond.sort()
    heart.sort()
    spade.sort()

    return club, diamond, heart, spade


def master_sort(lis):
    set1 = []
    break_indices = [0]
    odd_ones_out = []
    solved = []

    for i in lis[0:-1]:
       index = lis.index(i)
       if i == lis[index+1]-1 or i == lis[index-1]+1:
           set1.append(i)
       else:
           pass
    try:
        if lis[abs(len(lis)-1)] == lis[abs(len(lis)-2)]+1:
           set1.append(lis[len(lis)-1])
        else:
            pass
    except Exception as e:
        pass

    for i in lis:
        if i not in set1:
            odd_ones_out.append(i)
        else:
            pass



    for i in set1[0:-1]:
        if i + 1 != set1[set1.index(i)+1]:
            break_indices.append(set1.index(i)+1)

    length_to_split = []

    for i in range(len(break_indices)-1):
        x = break_indices[i+1]-break_indices[i]
        length_to_split.append(x)

    length_to_split.append(len(set1)-break_indices[-1])

    inputt = iter(set1)
    outputt = [list(islice(inputt, elem)) for elem in length_to_split]
    for i in outputt:
        if len(i) == 3 or len(i) == 4:
            solved.append(i)
        else:
            pass

    return outputt, odd_ones_out, solved


def print_text(player_dic):
    print(f"""
YOUR CARDS:
{player_dic}""")


def print_text_sort(club_outputt, club_odd_ones_out, club_solved, diamond_outputt, diamond_odd_ones_out, diamond_solved, heart_outputt, heart_odd_ones_out, heart_solved, spade_outputt, spade_odd_ones_out, spade_solved):
    print_text_sort_input = input("PRESS ANY KEY TO SORT YOUR CARDS SUIT WISE: ")
    print(f"""
YOUR CARDS ARRANGED SUIT WISE:

CLUB:
GROUPS: {club_outputt}
LEFTOVERS: {club_odd_ones_out}
SOLVED: {club_solved}

DIAMOND:
GROUPS: {diamond_outputt}
LEFTOVERS: {diamond_odd_ones_out}
SOLVED: {diamond_solved}

HEART:
GROUPS: {heart_outputt}
LEFTOVERS: {heart_odd_ones_out}
SOLVED: {heart_solved}

SPADE:
GROUPS: {spade_outputt}
LEFTOVERS: {spade_odd_ones_out}
SOLVED: {spade_solved}
""")



def left_over_choice_fn(left_over):
    give_left_over_input = input("PRESS ENTER TO SEE CARD THROWN BY COMPUTER: ")
    left_over_random = left_over[-1]
    print(f"""
CARD THROWN BY COMPUTER: {left_over_random}""")
    return left_over_random


def left_over_choice_fn_option(left_over, player_dic, left_over_random):
    error = True
    while error == True:
        left_over_card_user_input = input("Would you like to take this card (y/n): ")
        if left_over_card_user_input == "y":
            error = False
        elif left_over_card_user_input == "n":
            error = False
        else:
            error = True
            print("Invalid Input! Try again")
    

    if left_over_card_user_input == "y":
        error = True
        while error == True:
            left_over_card_replace = input("WHICH CARD DO YO U WANNA REPLACE?: ")
            if left_over_card_replace in player_dic:
                error = False
            else:
                error = True
        player_dic.remove(left_over_card_replace)
        player_dic.append(left_over_random)
        left_over.append(left_over_card_replace)

    elif left_over_card_user_input == "n":
        pass

    return left_over_card_user_input, player_dic, left_over

def common_set_choice_fn(common_set):
    give_common_set_input = input("PRESS ENTER TO SEE A CARD FROM COMMON SET: ")
    common_set_random = random.choice(common_set)
    print(f"""
CARD FROM COMMON SET: {common_set_random}""")
    return common_set_random


def common_set_choice_fn_option(common_set_random, player_dic, left_over, common_set):
    error = True
    while error == True:
        common_set_card_user_input = input("Would you like to take this card (y/n): ")

        if common_set_card_user_input == "y":
            error = False
        elif common_set_card_user_input == "n":
            error = False
        else:
            error = True
            print("Invalid Input! Try again")

    if common_set_card_user_input == "y":
        error = True
        while error == True:
                common_set_card_replace = input("WHICH CARD DO YO U WANNA REPLACE?: ")
                if common_set_card_replace in player_dic:
                    error = False
                else:
                    error = True
                    print("Invalid Input! Try Again")

        player_dic.remove(common_set_card_replace)
        player_dic.append(common_set_random)
        left_over.append(common_set_random)
        common_set.remove(common_set_random)

    elif common_set_card_user_input == "n":
        left_over.append(common_set_random)

    return player_dic, left_over

def left_over_choice_fn_comp(left_over):
    left_over_random = left_over[-1]
    return left_over_random


def left_over_choice_fn_option_comp(left_over, computer_dic, left_over_random):
    options = ["y", "n"]
    left_over_card_user_input = random.choice(options)
    if left_over_card_user_input == "y":
        left_over_card_replace = random.choice(computer_dic)
        computer_dic.remove(left_over_card_replace)
        computer_dic.append(left_over_random)
        left_over.append(left_over_card_replace)

    elif left_over_card_user_input == "n":
        pass

    return left_over_card_user_input, computer_dic, left_over


def common_set_choice_fn_comp(common_set):
    common_set_random = random.choice(common_set)
    return common_set_random


def common_set_choice_fn_option_comp(common_set_random, computer_dic, left_over, common_set):
    choices = ["y","n"]
    common_set_card_user_input = random.choice(choices)

    if common_set_card_user_input == "y":
        common_set_card_replace = random.choice(computer_dic)
        computer_dic.remove(common_set_card_replace)
        computer_dic.append(common_set_random)
        left_over.append(common_set_card_replace)
        common_set.remove(common_set_random)

    elif common_set_card_user_input == "n":
        left_over.append(common_set_random)

    return computer_dic, left_over

def solved_append(player_solved, suit_solved):
    if len(suit_solved) != 0:
        for i in suit_solved:
            player_solved.append(i)
    else:
        pass

    return player_solved



























