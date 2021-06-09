import test

def player_test(common_set, player_dic, left_over):
    test.print_text(player_dic)

    club, diamond, heart, spade = test.set_sort_strip(player_dic)

    club_outputt, club_odd_ones_out, club_solved = test.master_sort(club)
    diamond_outputt, diamond_odd_ones_out, diamond_solved = test.master_sort(diamond)
    heart_outputt, heart_odd_ones_out, heart_solved = test.master_sort(heart)
    spade_outputt, spade_odd_ones_out, spade_solved = test.master_sort(spade)

    test.print_text_sort(club_outputt, club_odd_ones_out, club_solved, diamond_outputt, diamond_odd_ones_out, diamond_solved, heart_outputt, heart_odd_ones_out, heart_solved, spade_outputt, spade_odd_ones_out, spade_solved)

    left_over_random = test.left_over_choice_fn(left_over)

    left_over_card_user_input, player_dic, left_over = test.left_over_choice_fn_option(left_over, player_dic, left_over_random)

    if left_over_card_user_input == "n":
        common_set_random = test.common_set_choice_fn(common_set)

        player_dic, left_over = test.common_set_choice_fn_option(common_set_random, player_dic, left_over)

    elif left_over_card_user_input == "y":
        pass

    player_solved = []
    player_solved = test.solved_append(player_solved, club_solved)
    player_solved = test.solved_append(player_solved, diamond_solved)
    player_solved = test.solved_append(player_solved, heart_solved)
    player_solved = test.solved_append(player_solved, spade_solved)

    return common_set, player_dic, left_over, player_solved


