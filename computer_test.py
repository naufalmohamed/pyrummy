import test

def computer_test(common_set, computer_dic, left_over):
    
    if len(common_set) == 0:
        for i in range(len(left_over)-1):
            common_set.append(i)
        else:
            pass

    # test.print_text(computer_dic)

    club, diamond, heart, spade = test.set_sort_strip(computer_dic)

    club_outputt, club_odd_ones_out, club_solved = test.master_sort(club)
    diamond_outputt, diamond_odd_ones_out, diamond_solved = test.master_sort(diamond)
    heart_outputt, heart_odd_ones_out, heart_solved = test.master_sort(heart)
    spade_outputt, spade_odd_ones_out, spade_solved = test.master_sort(spade)

    # test.print_text_sort(club_outputt, club_odd_ones_out, diamond_outputt, diamond_odd_ones_out, heart_outputt, heart_odd_ones_out, spade_outputt, spade_odd_ones_out)

    left_over_random = test.left_over_choice_fn_comp(left_over)

    left_over_card_user_input, computer_dic, left_over = test.left_over_choice_fn_option_comp(left_over, computer_dic, left_over_random)

    if left_over_card_user_input == "n":
        common_set_random = test.common_set_choice_fn_comp(common_set)

        computer_dic, left_over = test.common_set_choice_fn_option_comp(common_set_random, computer_dic, left_over, common_set)

    elif left_over_card_user_input == "y":
        pass

    comp_solved = []
    comp_solved = test.solved_append(comp_solved, club_solved)
    comp_solved = test.solved_append(comp_solved, diamond_solved)
    comp_solved = test.solved_append(comp_solved, heart_solved)
    comp_solved = test.solved_append(comp_solved, spade_solved)

    if len(comp_solved) == 3:

        club, diamond, heart, spade = test.set_sort_strip(computer_dic)

        club_outputt, club_odd_ones_out, club_solved = test.master_sort(club)
        diamond_outputt, diamond_odd_ones_out, diamond_solved = test.master_sort(diamond)
        heart_outputt, heart_odd_ones_out, heart_solved = test.master_sort(heart)
        spade_outputt, spade_odd_ones_out, spade_solved = test.master_sort(spade)
        
        comp_solved = []
        comp_solved = test.solved_append(comp_solved, club_solved)
        comp_solved = test.solved_append(comp_solved, diamond_solved)
        comp_solved = test.solved_append(comp_solved, heart_solved)
        comp_solved = test.solved_append(comp_solved, spade_solved)
    else:
        pass
        

    return common_set, computer_dic, left_over, comp_solved


